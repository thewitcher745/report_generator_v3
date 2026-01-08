position = 100
entry = 0.12299
mark = 0.1238
leverage = 20
commission_fee_rate = 0.05 / 100  # 0.05% commission

opening_fee = position * commission_fee_rate
margin = position / leverage - opening_fee
qty = position / entry
pnl = qty * (mark - entry)
pnl_percent = (pnl / margin) * 100
displayed_position = position + pnl

print(f"Margin: {margin}")
print(f"Displayed Position: {displayed_position}")
print(f"P&L: {pnl}")
print(f"P&L %: {pnl_percent:.2f}%")