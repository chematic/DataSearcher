# DataSearcher

A high-performance command-line utility designed to deeply scan large directories and file structures.  
DataSearcher provides powerful tools for indexing, collecting statistics, and rapidly locating specific content across extensive local data stores.

**Built for speed, efficiency, and large-scale file analysis.**

---

## ✨ Key Features

- **Adaptive Scanning (Auto Mode)**  
  Automatically selects the fastest search method (Simple, Threaded, or Indexed) based on the total size of the dataset.

- **Multi-threaded Analysis**  
  Uses multi-threading (up to your CPU core count) to significantly improve performance on medium-sized datasets.

- **In-Memory Indexing**  
  Supports indexing very large databases (1GB+ recommended) to enable near-instant searches after the initial indexing phase.

- **Detailed Statistics**  
  Displays total database size (GB), number of files, and number of folders at startup.

- **Result Saving**  
  Option to save all found matches to a timestamped file inside the dedicated `data/saves` directory.

---

## 🛠️ Installation

DataSearcher requires **Python 3.8 or higher**.

---

### 📦 Installation via Git Clone (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/chematic/datasearcher.git
```

2. Move into the project directory:
```bash
cd "datasearcher/Data Searcher"
```

3. Install dependencies:

**Windows**
```bash
requirements.bat
```

**Linux / macOS**
```bash
pip install pystyle requests
```

4. Launch the program:
```bash
python main.py
```

---

### ⚙️ Alternative Setup (Without Git)

#### A. Recommended (Windows)

Use the provided batch installer to handle dependencies automatically:

1. Run `requirements.bat`
2. It installs Python (if missing) and required modules (`pystyle`, `requests`)

#### B. Manual Installation (Linux / macOS or if A fails)

```bash
pip install pystyle requests
```

---

## 📁 Directory Structure

```
datasearcher/
├── main.py
├── requirements.bat
└── data/
    ├── datums/   <-- PLACE YOUR FILES HERE
    └── saves/    <-- RESULTS ARE SAVED HERE (AUTO-CREATED)
```

---

## 🚀 Usage

Run the main script from the root directory:

```bash
python main.py
```

### Interface Flow

1. **Startup**  
   Checks for updates and displays the application version along with statistics for `data/datums`.

2. **Query Input**  
   Enter the text string you want to search for.

3. **Mode Selection**

| Option | Method        | Description                              |
|------:|---------------|------------------------------------------|
| 1     | Simple Scan   | Sequential file scan                     |
| 3     | Threaded Scan | Multi-core scanning                      |
| 4     | Indexed Scan  | Loads all file contents into memory      |
| A     | Auto Mode     | Automatically selects the optimal method |

4. **Results Output & Saving**
- Displays total matches, unique files, and search duration
- Shows the top 20 results
- Prompts to save all results to `data/saves/`

---

## ⚠️ Important Note (Indexed Scan)

The **Indexed Scan (4)** and **Auto Mode** (for large datasets) load the entire contents of `data/datums` into RAM.

Ensure your system has sufficient available memory.

---

## 🛡️ License & Ownership Warning

**Ownership**  
The DataSearcher tool and all its internal fragments are the exclusive property of  
**@azunoo (Discord / Unique ID: 1400529025239220236)**.

**Restrictions**

- Modification of the source code is **strictly forbidden** without explicit permission
- Claiming ownership, removing attribution, or redistributing as your own work is **strictly forbidden**

---

**Auto Updater Notice**  
`c.py` will not modify the source code itself, at least for the time being.

---

Made by **@azunoo**
