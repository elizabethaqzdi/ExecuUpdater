# ExecuUpdater

ExecuUpdater is a lightweight tool that allows you to easily update executable files (.exe) with newer versions. It provides a graphical interface to select the file to update, specify the update URL, and automatically handles the update process with a backup and logging.

---

## Features

- **File Selection:** Select the executable file you want to update using the GUI.
- **Version Control:** Input the URL of the new version, and the tool will download and replace the old executable.
- **Automatic Backup:** Automatically creates a backup of the original file before updating.
- **Logging:** Provides a detailed log of actions and errors during the update process.

---

## How to Use

1. **Open the Tool:** Launch `ExecuUpdater.exe`.
2. **Select the File:** Use the "Browse" button to select the executable file you want to update.
3. **Enter Update URL:** Input the URL of the new version of the executable.
4. **Start Update:** Click the "Update" button to replace the old executable with the new version.
5. **Check Logs:** The log panel displays actions and errors for review.

---

## Prerequisites

- **Python (Optional):** The source code is written in Python using `tkinter` and `requests` modules.
- **Internet Connection:** Required to download the updated executable from the specified URL.

---

## Known Issues

- The tool does not validate the authenticity of the new version. Ensure you trust the URL before proceeding.
- Make sure the executable is not running during the update process to avoid errors.

---

## License

ExecuUpdater is distributed under the MIT License. Feel free to use, modify, and distribute it.

---

## Disclaimer

Use this tool responsibly. Always verify the source of new executable versions to prevent potential security risks.
