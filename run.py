#!/usr/bin/env python
"""
Entry point for Sign Language Detection API
Run this script from the project root to start the application
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Set PYTHONPATH environment variable for subprocess
os.environ['PYTHONPATH'] = project_root

if __name__ == "__main__":
    import uvicorn
    
    print(f"Starting Sign Language Detection API...")
    print(f"Project root: {project_root}")
    
    # Use string format so Uvicorn can properly reload the app
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True
    )
