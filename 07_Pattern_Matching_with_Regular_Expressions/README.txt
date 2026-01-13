 Regex Mastery & Security Validation

This section focuses on the "Three Pillars of Text Processing": Extraction, Sanitization, and Validation. These scripts demonstrate how to bridge the gap between raw string data and structured, verified information.



 📂 Featured Scripts

 1. Regex Date Auditor (`date_validator.py`)
 Concept: Semantic vs. Syntactic Validation.
 Logic: Extracts date patterns (`DD/MM/YYYY`) and then applies Gregorian calendar logic (leap years and month lengths) to ensure the date is physically possible.
 Key Tool: `re.VERBOSE` for documented pattern matching.

 2. Contact Information Scraper (`phoneAndEmail.py`)
 Concept: Practical Productivity Tools.
 Logic: Scans the system clipboard for complex phone formats (extensions, area codes) and RFCcompliant email addresses.
 Workflow: Automatically formats and recopies the filtered results for immediate use.

 3. Strict Sentence Validator (`sentence_check.py`)
 Concept: Grammar & Lexical Enforcement.
 Logic: Uses anchors (`^` and `$`) to force a fullstring match against a specific set of allowed subjects, verbs, and objects.
 Feature: Caseinsensitive matching via `re.I`.

 4. Regex Strip Clone (`regex_strip.py`)
 Concept: Reinventing the Wheel (For Science).
 Logic: Replicates the `string.strip()` method using regex substitution (`re.sub`).
 Technique: Dynamic construction of character classes based on userdefined "stripping" targets.

 5. Strong Password Auditor (`password_check.py`)
 Concept: Security Best Practices.
 Logic: A multipass validation engine that enforces length, casing diversity, and numeric inclusion.
 UX: Provides granular error reporting for specific security failures.



 🛠️ Technical Competencies

| Feature | Syntax | Application |
| : | : | : |
| Anchoring | `^` and `$` | Ensuring the entire string matches (no partials). |
| Substitution| `re.sub()` | Deleting or replacing text patterns. |
| Quantifiers | `{8,}` or `+` | Enforcing length or repetition requirements. |
| Character Sets| `[AZaz09]` | Defining allowed/disallowed lexical ranges. |
| Verbose Mode | `re.VERBOSE` | Breaking complex regex into readable, commented lines. |



 🚀 Execution
```bash
python phoneAndEmail.py   (Copy text to your clipboard first!)
python password_check.py