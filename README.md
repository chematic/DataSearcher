# DataSearcher

A high-performance command-line utility designed to deeply scan large directories and file structures.  
DataSearcher provides powerful tools for indexing, collecting statistics, and rapidly locating specific content across extensive local data stores.

**Built for speed, efficiency, and large-scale file analysis.**

---

## ✨ Key Features

- **Adaptive Scanning**  
  Automatically selects the fastest search method (Simple, Threaded, or Indexed) based on the total size of the dataset.

- **Multi-threaded Analysis**  
  Uses multi-threading to significantly improve performance on medium-sized datasets.

- **In-Memory Indexing**  
  Supports indexing very large databases (1GB+ recommended) to enable near-instant searches after the initial indexing phase.

- **Detailed Statistics**  
  Displays total database size (GB), number of files, and number of folders at startup.

- **Simple Command-Line Interface**  
  Clean and intuitive CLI for selecting scan modes and entering search queries.

---

## 🛠️ Installation

DataSearcher requires **Python 3.8 or higher**.

### Prerequisites

Install the required dependency for console formatting:

```bash
pip install pystyle
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/chematic/DataSearcher/datasearcher.git
cd datasearcher
```

2. Place your data in the following directory structure:
```
datasearcher/
├── main_script.py
└── data/
    └── datums/   <-- PLACE YOUR FILES HERE
```

---

## 🚀 Usage

Run the main script from the root directory:

```bash
python main.py
```

### Interface Flow

1. **Startup**  
   Displays the application version along with statistics for the data located in `data/datums`.

2. **Query Input**  
   Enter the text string you want to search for across all files.

3. **Mode Selection**  
   Choose a scanning method:

| Option | Method        | Description |
|------:|---------------|-------------|
| **1** | Simple Scan   | Standard sequential file scan |
| **3** | Threaded Scan | Multi-core scanning for faster execution |
| **4** | Indexed Scan  | Loads all file contents into memory |
| **A** | Auto Mode     | Automatically selects the optimal method (recommended) |

4. **Results Output**  
   Displays:
   - Total number of matches
   - Number of unique files containing the match
   - Search duration
   - Top 20 results in the format:  
     `[filepath:line_number] content`

---

## ⚠️ Important Note on Indexed Scan

The **Indexed Scan** (Option **4**) and **Auto Mode** (for large datasets) load the entire contents of the `data/datums` directory into RAM.

Ensure your system has sufficient memory to handle the reported dataset size.

---

Made by @azunoo
