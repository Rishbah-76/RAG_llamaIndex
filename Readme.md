**Project Name:**

RAG_MULTI_AGENT

**Purpose:**

we make the tools, we give it to the AI, and it will automatically decide the best tool to use. This is super cool, actually. Pretty easy to build. So in this demo you're going to see an agent who can answer questions about population and demographic data using something known as RAG. Now rag is retrieval augmented generation, and all this really means is that we're providing some extra data to the model, so that it can go and reason based off that rather than its old training data or something that might be out of date.
So in this instance, I've got two data sources which we're feeding to the model, and then there's another kind of thing it can do, which we'll talk about in a second. So we have this population data CSV file. Now this is structured data and it's typically pretty easy for our model to ingest this and read it. So this has pretty much all of the information about population density, the change, etc . and it will be able to kind of answer questions based on this CSV file. We then have a PDF specifically about India.

**Required Tools and Frameworks:**

* LlamaIndex version 
* Python version (e.g., 3.8 or later)
* Check req.txt for other packages

**Installation:**

**Recommended Method (using conda environment):**

1. **Create a conda environment:**

   ```bash
   conda create -n <environment_name> python=<python_version>
   conda activate <environment_name>
   ```

2. **Clone the repository:**

   ```bash
   git clone <repository_URL>
   ```

3. **Install dependencies:**

   ```bash
   pip install -r req.txt
   ```

4. **Set up an `.env` file (optional, if needed):**

   - Create a `.env` file in the root directory.
   - Add any sensitive information required by your code, such as API keys, in the following format:

     ```
     OPENAI_API_KEY=your_api_key
     # Add other environment variables as needed
     ```

   - This enhances security by keeping credentials outside the public repository.

**Alternative Method (using pip):**

1. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv <environment_name>
   source <environment_name>/bin/activate
   ```

2. **Clone the repository:**

   ```bash
   git clone <repository_URL>
   ```

3. **Install dependencies:**

   ```bash
   pip install -r req.txt
   ```

**Running the Code:**

1. **Navigate to the project directory:**

   ```bash
   cd <project_directory>
   ```

2. **Execute the main script:**

   ```bash
   python main.py
   ```

