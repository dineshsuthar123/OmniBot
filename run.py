import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get port from environment or use default 8000
    port = int(os.getenv("PORT", 8000))
    
    # Run the FastAPI app with uvicorn, binding to the environment port
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=port,  # Use the port from environment
        reload=True
    )
