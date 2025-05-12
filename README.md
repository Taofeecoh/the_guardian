# Hola Open Source Enthusiast!👋
# 📰 the_guardian

**the_guardian** is a Python-based data pipeline designed to fetch and process Nigerian news articles from The Guardian. It includes modules for data ingestion, transformation, and storage.

📌 Tech Stack used: Python 3.12, Libraries & Modules, Third Party API, GIT, VS Code

## 📁 Project Structure

- `guardian_pipeline.py`: Main script orchestrating the data pipeline.
- `guardianmodule.py`: Contains utility functions used across the pipeline.
- `guardian_NigerianArticles.csv`: Dataset containing Nigerian news articles.
- `requirements.txt`: Lists Python dependencies.
- `Dockerfile`: Configuration for containerizing the application.

## 📃 Contents
>Installation
1. Fork the project 🔪
2. Clone the forked repository 📥
3. Setup 🔧⚙️
4. Installing packages required 📦📥
> Usage
5. Generate API key
6. Store environment variables
7. Execute

## ⚙️ Installation
1. **Fork the project repository**
2. **Clone (download) the repository on your local machine:**

   ```bash
   $ git clone https://github.com/Taofeecoh/the_guardian.git
   ```

   **Move into the direcctory with the clone repository:**

   ```
   $ cd the_guardian
   ```

3. **Set up a virtual environment (optional but highly recommended):**

   ```bash
   the_guardian$ python -m venv venv
   ```
   **Activate environment**

   ```bash
   the_guardian$ source venv/bin/activate  

   # On Windows: 
   venv\Scripts\activate
   ```

4. **Install the required packages:**

   ```bash
   $ pip install -r requirements.txt
   ```

## 🚀 Usage
5. **Generate access key**

Before running the ```guardian_pipeline.py``` script, we need create a developer account on the guardian open platform [website](https://open-platform.theguardian.com/access/) in order to generate our **API key**.

6. **Store environment variables**
   In the same working directory, create a ```.env``` file.

   ```bash
   the_guardian$ touch .env 
   ```
   In the created file, define a variable like below and assign the API key to it.
   ```bash
   GUARDIAN_KEY="<API_key>"
   ```

7. **Execute**

To execute the data pipeline and store in s3 if there is a valid AWS user account:

```bash
python guardian_pipeline.py # Or python3 guardian_pipeline.py
```
Else, comment out everything from the session portion of the code downward as demonstrated below to fetch data in a csv in the working directory:

```python
# session = boto3.Session(
#     aws_access_key_id=os.getenv("ID"),
#     aws_secret_access_key=os.getenv("KEY")
# )

# my_path = "s3://taofeecoh-bucket"
# wr.s3.to_parquet(
#     df=df,
#     path=f"{my_path}/app4/nigerian-guardian:v1",
#     boto3_session=session,
#     mode="append",
#     dataset=True
#     )

```

## 🤝 Contributing

Contributions are welcome! Please submit a pull request with your enhancements.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
