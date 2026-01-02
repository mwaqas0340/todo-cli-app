# 📝 In Memory Python Console App

A **spec-driven, in-memory Python CLI Todo application** built to practice clean architecture, disciplined development, and AI-assisted workflows using **Spec-Kit Plus** and **Claude Code**.

This project intentionally avoids files, databases, and external libraries to keep the focus on **core Python logic, CLI design, and professional development process**.

---

## 🎯 Project Goals

* Practice **Spec-Driven Development (SDD)**
* Build a clean and reliable **Python Console (CLI) application**
* Learn how to control AI coding tools using **clear specifications**
* Focus on **logic, structure, and correctness** instead of frameworks

---

## 📌 Key Characteristics

* ✅ In-memory storage only (data is lost on exit)
* ✅ Menu-based CLI interface
* ✅ Beginner-friendly but professional code structure
* ✅ No external libraries
* ✅ No feature creep (strictly spec-compliant)

---

## 🚀 Features (Final Scope)

The application supports **ONLY** the following features:

1. **Add Todo**

   * Add a new todo with a title (required)
   * Optional description

2. **View Todos**

   * Display all todos in a readable format
   * Gracefully handles empty todo list

3. **Update Todo**

   * Update title, description, or both
   * Empty input does not overwrite existing data
   * Handles invalid IDs safely

4. **Delete Todo**

   * Delete a todo by ID
   * Handles non-existent IDs with error messages

5. **Exit Application**

   * Safely terminates the program

❌ Mark Complete
❌ File or Database Storage
❌ GUI / Web Interface
❌ External Dependencies

---

## 🧠 Todo Data Model (Conceptual)

Each Todo item contains:

* `id` → Auto-incremented integer (unique)
* `title` → String (required)
* `description` → String (optional)

All todos are stored **only in memory** using basic Python data structures.

---

## 🗂️ Suggested Project Structure

```text
in_memory_todo/
│
├── specs/
│   └── todo.spec.md
│
├── app/
│   ├── main.py            # CLI loop and menu handling
│   ├── todo_manager.py   # Business logic
│   └── models.py         # Todo data model
│
└── README.md
```

---

## 🧪 Development Methodology

This project follows **Spec-Kit Plus**, using the following disciplined workflow:

```text
sp.constitution  →  sp.specification  →  sp.planning  →  sp.tasks  →  sp.implement
```

### Why This Matters

* Prevents unclear requirements
* Stops unnecessary features
* Improves AI-generated code quality
* Mimics real-world software development practices

---

## 🤖 AI Tools Used

* **Claude Code** → Implementation partner
* **Spec-Kit Plus** → Requirement & planning framework

The AI is treated as a **junior developer** that must strictly follow specifications.

---

## ▶️ How to Run

1. Ensure Python is installed (Python 3.x)
2. Navigate to the project directory
3. Run the CLI application:

```bash
python app/main.py
```

---

## 🖥️ Example CLI Menu

```text
======== TODO APP ========
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Exit
=========================
Select option:
```

---

## 🧯 Error Handling Philosophy

* Invalid menu input → Friendly error message
* Invalid Todo ID → Clear warning
* Empty todo list → Informative message
* App never crashes due to user input

---

## 🎓 What You Will Learn from This Project

* Clean Python function design
* CLI-based user interaction
* In-memory data handling
* Defensive programming
* Spec-driven & AI-assisted development

This project is **interview-friendly** and ideal for strengthening core programming fundamentals.

---

## 🔮 Possible Future Extensions (Not Implemented)

> These are intentionally excluded to preserve scope discipline:

* File-based persistence
* Mark complete feature
* Search / filter
* Command-based CLI
* Unit testing

---

## 📜 License

This project is intended for **learning and practice purposes**.
You are free to modify and extend it for personal use.

---

## ✨ Final Note

This repository is not just a Todo app — it is a **thinking exercise** in how real software should be planned, specified, and built.

**Simple app. Strong process. Professional mindset.**
