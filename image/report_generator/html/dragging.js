// This function adds drag and drop functionality to the text elements of the report.
// It is self-invoking, so it doesn't need to be called.

(
    function () {
        console.log("Drag and drop enabled.")
        let lastClickedElement = null;
        
        function toPx(n) {
            return Number.isFinite(n) ? n + 'px' : '0px';
        }

        function getNumberPx(value) {
            if (!value) return 0;
            if (typeof value === 'number') return value;
            const m = String(value).match(/-?\d+(?:\.\d+)?/);
            return m ? parseFloat(m[0]) : 0;
        }
        
        function enableDrag(el) {
            
                el.style.cursor = 'move';
                el.style.userSelect = 'none';

                let startX = 0, startY = 0;
                let startLeft = 0, startTop = 0;
                let dragging = false;

                function onPointerDown(clientX, clientY, e) {
                    // Reset previous clicked element styles
                    if (lastClickedElement && lastClickedElement !== el) {
                        lastClickedElement.style.color = '';
                        lastClickedElement.style.opacity = '';
                    }
                    
                    lastClickedElement = el;
                    const cs = window.getComputedStyle(el);
                    startLeft = getNumberPx(el.style.left || cs.left);
                    startTop = getNumberPx(el.style.top || cs.top);
                    startX = clientX;
                    startY = clientY;
                    dragging = true;
                    
                    // Apply red background and 50% opacity
                    el.style.color = 'red';
                    el.style.opacity = '0.5';
                    e.preventDefault();
                }

                function onPointerMove(clientX, clientY) {
                    if (!dragging) return;
                    const dx = clientX - startX;
                    const dy = clientY - startY;
                    el.style.left = toPx(startLeft + dx);
                    el.style.top = toPx(startTop + dy);
                }

                function onMouseDown(e) { onPointerDown(e.clientX, e.clientY, e); }
                function onMouseMove(e) { onPointerMove(e.clientX, e.clientY); }
                function onMouseUp() {
                    if (!dragging) return; // only act for the element that was dragging

                    const bBox = document.querySelector("img").getBoundingClientRect();
                    const imageWidth = bBox.width;
                    const imageHeight = bBox.height;
                    
                    const rect = el.getBoundingClientRect();
                    const parentRect = el.parentElement.getBoundingClientRect();
                    const x = (rect.left - parentRect.left) / imageWidth;
                    const y = (rect.top - parentRect.top) / imageHeight;
                    console.log(`x=${x}, y=${y}`);
                    dragging = false;
                }

                el.addEventListener('mousedown', onMouseDown);
                window.addEventListener('mousemove', onMouseMove);
                window.addEventListener('mouseup', onMouseUp);
        }

        document.addEventListener('DOMContentLoaded', function () {
          document.body.querySelectorAll('*:not(#bg):not(script):not(#report)').forEach(enableDrag);
          
          // Add keyboard event listener for arrow keys
          document.addEventListener('keydown', function(e) {
              if (!lastClickedElement) return;
              
              const cs = window.getComputedStyle(lastClickedElement);
              let currentLeft = getNumberPx(lastClickedElement.style.left || cs.left);
              let currentTop = getNumberPx(lastClickedElement.style.top || cs.top);
              
              switch(e.key) {
                  case 'ArrowUp':
                      e.preventDefault();
                      lastClickedElement.style.top = toPx(currentTop - 0.5);
                      break;
                  case 'ArrowDown':
                      e.preventDefault();
                      lastClickedElement.style.top = toPx(currentTop + 0.5);
                      break;
                  case 'ArrowLeft':
                      e.preventDefault();
                      lastClickedElement.style.left = toPx(currentLeft - 0.5);
                      break;
                  case 'ArrowRight':
                      e.preventDefault();
                      lastClickedElement.style.left = toPx(currentLeft + 0.5);
                      break;
              }
          });
        });
    }
)();