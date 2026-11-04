# มาโครพิมพ์คำสั่ง fline อัตโนมัติ
# กด Ctrl + Shift + 1-6 เพื่อพิมพ์คำสั่ง
# กด Ctrl + Shift + Q เพื่อปิดโปรแกรม
#
# [ctrl] + [shift] + [1] = fline(85, 85, 0.75, "a0", 'f', 'l', 80, "a2", 1);
# [ctrl] + [shift] + [2] = fline(85, 85, 0.75, "a7", 'f', 'r', 80, "a5", 1);
# [ctrl] + [shift] + [3] = fline(50, 50, 0.75, "a0", 'c', 'l', 70, "a1", 10);
# [ctrl] + [shift] + [4] = fline(50, 50, 0.75, "a7", 'c', 'r', 70, "a6", 10);
# [ctrl] + [shift] + [5] = fline(20, 20, 0.75, "a7", 'f', 's', 80, "a5", 10);
# [ctrl] + [shift] + [6] = fline(85, 85, 0.85, "a7", 'f', 'p', 80, "a5", 0);
#
# ต้องการเปลี่ยนค่า: แก้ข้อความในรายการ MACROS ด้านล่าง

import keyboard

MACROS = {
    'ctrl+shift+1': 'fline(85, 85, 0.75, "a0", \'f\', \'l\', 80, "a2", 1);',
    'ctrl+shift+2': 'fline(85, 85, 0.75, "a7", \'f\', \'r\', 80, "a5", 1);',
    'ctrl+shift+3': 'fline(50, 50, 0.75, "a0", \'c\', \'l\', 70, "a1", 10);',
    'ctrl+shift+4': 'fline(50, 50, 0.75, "a7", \'c\', \'r\', 70, "a6", 10);',
    'ctrl+shift+5': 'fline(20, 20, 0.75, "a7", \'f\', \'s\', 80, "a5", 10);',
    'ctrl+shift+6': 'fline(85, 85, 0.85, "a7", \'f\', \'p\', 80, "a5", 0);',
}


def auto_type(text):
    keyboard.write(text)


for hotkey, text in MACROS.items():
    keyboard.add_hotkey(hotkey, lambda t=text: auto_type(t))

print("--- โปรแกรมเริ่มทำงานแล้ว ---")
for hotkey, text in MACROS.items():
    print(f"  {hotkey:<14} -> {text}")
print("  ctrl+shift+q   -> ปิดโปรแกรม")

keyboard.wait('ctrl+shift+q')
print("--- ปิดโปรแกรมแล้ว ---")
