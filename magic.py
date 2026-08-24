import os
import subprocess
import ollama

print("\n--- PROMPT TO BINARY ENGINE V4 (AUTO-FIX MULTI-AGENT) TAIYAAR HAI ---")
user_idea = input("Bhai, tujhe kaisa software (C language) banana hai? ")

max_retries = 3
current_attempt = 1
ai_code = ""
compiler_error = ""

while current_attempt <= max_retries:
    if current_attempt == 1:
        print("\n[AI Coder Soch Raha Hai...] Pehli baar code likha ja raha hai...")
        prompt = f"Write ONLY a complete, working C program code for: {user_idea}. Give ONLY the raw C code starting with #include. No markdown, no text."
    else:
        print(f"\n[AI Fixer Soch Raha Hai...] Attempt {current_attempt}/{max_retries}: Puraani galti theek ki ja rahi hai...")
        # AI 2 ko error aur purana code bhej rahe hain
        prompt = f"The following C code failed to compile.\n\nCOMPILER ERROR:\n{compiler_error}\n\nBUGGY CODE:\n{ai_code}\n\nPlease fix the syntax error and provide ONLY the corrected raw C code. Do not use markdown format. Do not explain anything."

    try:
        response = ollama.chat(model='qwen2.5-coder:1.5b', messages=[
          {'role': 'user', 'content': prompt}
        ])
        
        ai_code = response['message']['content']

        # --- MAGIC CLEANER (Filter) ---
        if "```c" in ai_code:
            ai_code = ai_code.split("```c")[1].split("```")[0]
        elif "```" in ai_code:
            ai_code = ai_code.split("```")[1].split("```")[0]
        ai_code = ai_code.strip()
        # ------------------------------

        # Temporary file mein code dalna
        with open("temp.c", "w") as file:
            file.write(ai_code)

        print("[Compiler Test...] TCC error check kar raha hai...")
        
        # NOTE: Yahan humne capture_output=True lagaya hai taaki hum error padh sakein!
        result = subprocess.run(["tcc", "temp.c", "-o", "tera_app.exe"], capture_output=True, text=True)

        if result.returncode == 0:
            os.remove("temp.c")
            print(f"\n✅ SUCCESS! Attempt {current_attempt} mein AI ne ekdum sahi code likha!")
            print("Bhai tera 'tera_app.exe' taiyaar hai! Source Code mita diya gaya hai.")
            break  # Kaam ho gaya, Loop tod do!
        else:
            # Compiler fail hua, error save karo aur agli baar AI ko do
            compiler_error = result.stderr
            print(f"❌ OOPS! Compiler ko galti mili: {compiler_error.strip().splitlines()[0]}")
            print("Error wapas AI ko bheja ja raha hai theek karne ke liye...")
            current_attempt += 1

    except Exception as e:
        print("\nERROR: Ollama chalne mein dikkat aayi.")
        print(e)
        break

if current_attempt > max_retries:
    print("\n⚠️ Bhai, AI ne 3 baar koshish ki par ye complex logic theek nahi kar paya. Ya toh prompt chota kar, ya bada AI model (7B) download kar.")