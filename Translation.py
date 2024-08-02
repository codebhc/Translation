import tkinter as tk
from tkinter import ttk
from translate import Translator

# 创建一个包含语言名称和对应代码的字典
language_codes = {
    "英语": "en",
    "简体中文": "zh-CN",
    "繁体中文": "zh-TW",
    "维吾尔语": "ug",
    "西班牙语": "es",
    "法语": "fr",
    "德语": "de",
    "阿拉伯语": "ar",
    "俄语": "ru",
    "日语": "ja",
    "韩语": "ko",
    "葡萄牙语": "pt",
    "意大利语": "it",
    "印地语": "hi",
    "孟加拉语": "bn",
    "印尼语": "id",
    "土耳其语": "tr",
    "波兰语": "pl",
    "波斯语": "fa",
    "乌克兰语": "uk",
    "泰语": "th",
    "越南语": "vi",
    "罗马尼亚语": "ro",
    "荷兰语": "nl",
    "捷克语": "cs",
    "希腊语": "el",
    "匈牙利语": "hu",
    "瑞典语": "sv",
    "芬兰语": "fi",
    "丹麦语": "da",
    "挪威语": "no",
    "希伯来语": "he",
    "阿拉伯语": "ar",
    "乌尔都语": "ur",
    "泰卢固语": "te",
    "马拉地语": "mr",
    "泰米尔语": "ta",
    "旁遮普语": "pa",
    "古吉拉特语": "gu",
    "卡纳达语": "kn",
    "马拉雅拉姆语": "ml",
    "奥里亚语": "or",
    "孟加拉语": "bn",
    "阿萨姆语": "as",
    "马拉地语": "mr",
    "印地语": "hi",
    "古吉拉特语": "gu",
    "泰卢固语": "te",
    "泰米尔语": "ta",
    "旁遮普语": "pa",
    "卡纳达语": "kn",
    "马拉雅拉姆语": "ml",
    "奥里亚语": "or",
    "孟加拉语": "bn",
    "阿萨姆语": "as",
    "越南语": "vi"
}

def translate_text():
    text_to_translate = input_text.get("1.0", tk.END)
    source_language = language_codes[from_language_combo.get()]
    target_language = language_codes[to_language_combo.get()]
    translator = Translator(from_lang=source_language, to_lang=target_language)

    # 显示“正在翻译”状态
    status_label.config(text="")

    try:
        translated_text = translator.translate(text_to_translate)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)

        # 显示“翻译完成”状态，两秒后自动消失
        status_label.config(text="翻译完成")
        root.after(2000, lambda: status_label.config(text=""))
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"错误: {e}")

def show_placeholders(event):
    if input_text.get("1.0", tk.END).strip() == "":
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, "请输入你要翻译的内容")
        input_text.config(fg="gray")
    if output_text.get("1.0", tk.END).strip() == "":
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "内容翻译完会在这里显示")
        output_text.config(fg="gray")

def hide_placeholders(event):
    if input_text.get("1.0", tk.END).strip() == "请输入你要翻译的内容":
        input_text.delete("1.0", tk.END)
        input_text.config(fg="black")
    if output_text.get("1.0", tk.END).strip() == "内容翻译完会在这里显示":
        output_text.delete("1.0", tk.END)
        output_text.config(fg="black")

# 设置主应用窗口
root = tk.Tk()
root.title("多语言翻译器")
root.geometry("800x600")
root.configure(bg='lightgray')

# 创建用于用户输入的文本窗口
input_label = tk.Label(root, text="输入文本:", font=("Arial", 14), bg='lightgray')
input_label.pack(pady=10)
input_text = tk.Text(root, height=5, width=40, font=("Arial", 12))
input_text.pack()
input_text.insert(tk.END, "请输入你要翻译的内容")
input_text.config(fg="gray")
input_text.bind("<FocusIn>", hide_placeholders)
input_text.bind("<FocusOut>", show_placeholders)

# 创建一个框架，用于放置语言选择ComboBox
language_frame = tk.Frame(root, bg='lightgray')
language_frame.pack(pady=10)

# 创建ComboBox，用于选择翻译来源语言
from_language_label = tk.Label(language_frame, text="源语言:", font=("Arial", 14), bg='lightgray')
from_language_label.pack(side=tk.LEFT)
from_language_combo = ttk.Combobox(language_frame, values=list(language_codes.keys()), state="readonly", font=("Arial", 12))
from_language_combo.set("简体中文")
from_language_combo.pack(side=tk.LEFT)

# 创建ComboBox，用于选择翻译目标语言
to_language_label = tk.Label(language_frame, text="目标语言:", font=("Arial", 14), bg='lightgray')
to_language_label.pack(side=tk.LEFT)
to_language_combo = ttk.Combobox(language_frame, values=list(language_codes.keys()), state="readonly", font=("Arial", 12))
to_language_combo.set("维吾尔语")
to_language_combo.pack(side=tk.LEFT)

# 创建按钮，用于触发翻译
translate_button = tk.Button(root, text="翻译", command=translate_text, font=("Arial", 14), bg='lightblue', fg='white')
translate_button.pack(pady=10)

# 创建一个标签，用于显示翻译状态
status_label = tk.Label(root, text="", font=("Arial", 12), bg='lightgray')
status_label.pack(pady=10)

# 创建文本窗口，用于显示翻译结果
output_label = tk.Label(root, text="翻译结果:", font=("Arial", 14), bg='lightgray')
output_label.pack()
output_text = tk.Text(root, height=5, width=40, bg="light cyan", font=("Arial", 12))
output_text.pack()
output_text.insert(tk.END, "内容翻译完会在这里显示")
output_text.config(fg="gray")
output_text.bind("<FocusIn>", hide_placeholders)
output_text.bind("<FocusOut>", show_placeholders)

# 启动Tkinter主循环
root.mainloop()
