# Git Instructions

## Cloning this Repository

1. **Prerequisite**
   - Ensure you have Git installed on your computer. You can download it from [git-scm.com](git-scm.com).
2. **Go to the Repository's Home Page**
   - Open your web browser and navigate to [our class GitHub repository](https://github.com/narcisolobo/python-june-2024).
   - You should be on [the repository's main page](https://github.com/narcisolobo/python-june-2024), which displays the code files and folders.

3. **Locate the "Code" Button**
   - On the repository home page, find the green "Code" button. It's usually located near the top right of the file list.

4. **Copy the Repository URL**
   - Click the "Code" button. A dropdown menu will appear.
   - Under the "HTTPS" tab, you will see a URL. This is the repository URL.
   - Click the clipboard icon next to the URL to copy it. The URL should be: `https://github.com/narcisolobo/python-june-2024.git`.

5. **Open Your Terminal or Command Prompt**
   - If you're using Windows, open Command Prompt or PowerShell.
   - If you're on a Mac or Linux, open Terminal.

6. **Navigate to Your Desired Directory**
   - Use the `cd` command to change to the directory where you want to clone the repository.
   - For example, to navigate to your Desktop, type `cd Desktop` and press Enter.

7. **Clone the Repository**
   - In the terminal or command prompt, type `git clone` followed by a space, then paste the repository URL you copied earlier.
   - It should look like this: `git clone https://github.com/narcisolobo/python-june-2024.git`
   - Press Enter. Git will start cloning the repository to your current directory.

8. **Access the Cloned Repository**
   - Once the cloning process is complete, you will have a new folder in your current directory with the repository's name.
   - To navigate into this new folder, use the `cd` command followed by the repository name.
   - For example: `cd repository`

## How to Pull the Latest Code

1. **Open Your Terminal or Command Prompt**
   - Ensure your terminal or command prompt is open and you are in the cloned repository's directory.

2. **Pull the Latest Code**
   - In the terminal or command prompt, type:
      ```sh
      git pull
      ```
3. **Stay Up-to-Date**
   - Regularly use `git pull` to keep your local repository up-to-date with the latest changes from the remote repository. 

## Configuring Git Username and Email
The following commands may be run from any location in your terminal/shell of choice. You only need to do this once.

1. **Set Your Username**
    ```sh
    git config --global user.name "Your GitHub Username"
    ```
2. **Set Your Email**
    ```sh
    git config --global user.email "your-github-email@example.com"
    ```