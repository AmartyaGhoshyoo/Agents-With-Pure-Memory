import sqlite3
import os
import json

def explore_sqlite_db():
    """Explore the SQLite agent.db file"""
    print("=" * 60)
    print("EXPLORING SQLITE DATABASE (agent.db)")
    print("=" * 60)
    
    # Use absolute path
    db_path = "/Users/amartyaghosh/Agents with Memory/agno_agentic.db"
    
    if not os.path.exists(db_path):
        print(f"Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"Tables found: {[table[0] for table in tables]}")
        print()
        
        for table in tables:
            table_name = table[0]
            print(f"Table: {table_name}")
            print("-" * 40)
            
            # Get table schema
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            print("Columns:")
            for col in columns:
                print(f"  {col[1]} ({col[2]})")
            print()
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"Row count: {count}")
            
            # Show sample data (first 5 rows)
            if count > 0:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
                rows = cursor.fetchall()
                print("Sample data:")
                for i, row in enumerate(rows):
                    print(f"  Row {i+1}: {row}")
            print()
            
        conn.close()
        
    except Exception as e:
        print(f"Error exploring SQLite database: {e}")

def explain_lancedb_structure():
    """Explain what each LanceDB directory contains"""
    print("=" * 60)
    print("LANCEDB STRUCTURE EXPLANATION")
    print("=" * 60)
    
    lancedb_path = "/Users/amartyaghosh/Library/Mobile Documents/com~apple~TextEdit/Documents/Projects ML/Heart Disease Prediction/Agentic AI/Agentic -AI- Agents/Agno/AgAgents Leaning Notes/tmp/lancedb/agno_docs.lance"
    
    print("LanceDB Directory Structure:")
    print()
    
    # Explain each directory
    directories = {
        "_indices": {
            "purpose": "Contains search indices for fast vector similarity search",
            "files": "Fast search index files (.fast, .idx, .store, .term, .pos)",
            "explanation": "These files enable the agent to quickly find relevant text chunks when searching the knowledge base"
        },
        "_versions": {
            "purpose": "Contains version manifests for tracking changes and rollbacks",
            "files": "Version manifest files (.manifest)",
            "explanation": "Each .manifest file represents a snapshot of the database at a specific point in time, enabling version control and rollbacks"
        },
        "_transactions": {
            "purpose": "Contains transaction logs for ACID compliance and data integrity",
            "files": "Transaction files (.txn)",
            "explanation": "These files log all database operations to ensure data consistency and allow recovery from failures"
        },
        "data": {
            "purpose": "Contains the actual data chunks in Lance format",
            "files": "Data files (.lance)",
            "explanation": "Each .lance file contains the actual text chunks and their vector embeddings from the Agno documentation"
        }
    }
    
    for dir_name, info in directories.items():
        dir_path = os.path.join(lancedb_path, dir_name)
        if os.path.exists(dir_path):
            file_count = len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])
            print(f"{dir_name}/:")
            print(f"  Purpose: {info['purpose']}")
            print(f"  Files: {file_count} files")
            print(f"  File types: {info['files']}")
            print(f"  Explanation: {info['explanation']}")
            
            # Show some sample files
            if file_count > 0:
                sample_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))][:3]
                print(f"  Sample files: {sample_files}")
            print()
        else:
            print(f"{dir_name}/: Directory not found")
            print()

def show_file_counts():
    """Show the count of files in each LanceDB directory"""
    print("=" * 60)
    print("LANCEDB FILE COUNTS")
    print("=" * 60)
    
    lancedb_path = "/Users/amartyaghosh/Library/Mobile Documents/com~apple~TextEdit/Documents/Projects ML/Heart Disease Prediction/Agentic AI/Agentic -AI- Agents/Agno/AgAgents Leaning Notes/tmp/lancedb/agno_docs.lance"
    
    for dir_name in ["_indices", "_versions", "_transactions", "data"]:
        dir_path = os.path.join(lancedb_path, dir_name)
        if os.path.exists(dir_path):
            files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
            print(f"{dir_name}/: {len(files)} files")
            
            # Group files by extension
            extensions = {}
            for file in files:
                ext = os.path.splitext(file)[1]
                extensions[ext] = extensions.get(ext, 0) + 1
            
            for ext, count in extensions.items():
                print(f"  {ext}: {count} files")
        else:
            print(f"{dir_name}/: Directory not found")
        print()

if __name__ == "__main__":
    print("AGNO DATABASE EXPLORER")
    print("=" * 60)
    
    # Explore SQLite database
    explore_sqlite_db()
    
    # Explain LanceDB structure
    explain_lancedb_structure()
    
    # Show file counts
    show_file_counts()
    
    print("=" * 60)
    print("EXPLORATION COMPLETE")
    print("=" * 60)