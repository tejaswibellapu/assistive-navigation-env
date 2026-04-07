from fastapi import FastAPI
from my_env.env import AssistiveEnv
import uvicorn

app = FastAPI()
env = AssistiveEnv()


@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs.description}


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()