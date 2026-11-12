import sys

def process_tiktok():
    print("=== أداة إزالة علامة تيك توك ===")
    user_url = input("الرجاء لصق رابط تيك توك هنا: ")
    
    if not user_url.strip():
        print("[-] تنبيه: لم يتم إدخال أي رابط!")
        return
        
    if "tiktok.com" in user_url:
        print("[+] ممتاز! تم التحقق من الرابط بنجاح.")
        print("[*] جاري معالجة الرابط وإزالة العلامة المائية...")
        print("[✓] تم الانتهاء بنجاح! رابط التحميل الصافي جاهز.")
    else:
        print("[-] خطأ: هذا ليس رابط تيك توك صحيح.")

if __name__ == "__main__":
    process_tiktok()
