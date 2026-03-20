Here is the **complete professional workflow** you must follow every time you:

- add a new person
- change code
- update database
- run the face recognition system

This is the **standard operating procedure (SOP)**.

---

# 📁 Project Structure (must always look like this)

```text
face_recongnition_system/
│
├── .venv/
├── main.py
│
├── dataset/
│   ├── person1.jpg
│   ├── person2.jpg
│   ├── person3.jpg
│   └── newperson.jpg   ← add new faces here
│
├── database/
│   └── users.json
```

---

# 🧑‍💻 STEP 1: Add new person image

Put image in:

```text
dataset/
```

Example:

```text
dataset/person4.jpg
```

IMPORTANT rules:

- Image must contain clear face
- Only ONE face per image
- File name = person ID

Example:

```text
person4.jpg
```

---

# 🧾 STEP 2: Add person info in database

Open:

```text
database/users.json
```

Add new entry:

```json
{
  "person1": {
    "name": "Vishnu",
    "age": "23",
    "id": "EMP001"
  },
  "person2": {
    "name": "Rahul",
    "age": "25",
    "id": "EMP002"
  },
  "person4": {
    "name": "John",
    "age": "30",
    "id": "EMP004"
  }
}
```

IMPORTANT:

```text
filename = person4.jpg
json key = person4
```

Must match.

---

# ▶️ STEP 3: Run system (ALWAYS follow this)

Open PowerShell and set your working directory:

```powershell
cd "D:\Data Science OF\FaceDetectionProject\Complete Face Detection\face_recongnition_system"
```

Activate virtual environment (if not already active):

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the system:

```powershell
python main.py
```

Expected output:

- Loading dataset...
- Loaded: personX for each image
- Dataset loaded successfully
- System started. Press ESC or close window to exit.

If the camera is not accessible, close other camera apps and retry.

Exit command (in the GUI window): ESC or close window.

---

# 📷 STEP 4: System will show output

Example:

```text
Loading dataset...
Loaded: person1
Loaded: person2
Loaded: person4
Dataset loaded successfully
System started.
```

Camera opens.

Shows:

```text
John | Age:30 | ID:EMP004
```

---

# 🔁 STEP 5: Every time you add new person

You ONLY need to do:

```powershell
cd face_recongnition_system
.\.venv\Scripts\Activate.ps1
python main.py
```

No reinstall required.

---

# 🛠 STEP 6: If you modify code

Just save file and run again:

```powershell
python main.py
```

---

# ❌ NEVER do this again

```powershell
pip install face_recognition_models   ❌
pip install face_recognition         ❌
```

Already installed.

---

# ⚡ OPTIONAL: Auto reload method (developer method)

Install watchdog:

```powershell
pip install watchdog
```

Run:

```powershell
watchmedo auto-restart --patterns="*.py" -- python main.py
```

Auto restarts when code changes.

---

# 🧠 Summary workflow

```text
Add image → dataset/
Add info → users.json
Run → python main.py
Done
```

---

# ✅ Example adding new person

Step 1:

```text
dataset/person5.jpg
```

Step 2:

```json
"person5": {
    "name": "Alice",
    "age": "28",
    "id": "EMP005"
}
```

Step 3:

```powershell
python main.py
```

Done.

---
