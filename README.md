# Image Migrator
A Python script to help AI enthusiasts reclaim disk space by migrating large collections of generated images to a secondary drive.

___

> [!CAUTION]
> **A Word of Warning: Advanced Users Only!**
>
> The following script is a powerful tool that can move and alter thousands of files on your system. It is provided "as-is" with no guarantees. If you are not comfortable with Python or editing scripts to match your specific system, **DO NOT USE IT.** We are not responsible for any data loss.

> [!WARNING]
> **Before you proceed, you must understand the following:**
>
> *   **Know Your System:** This script assumes a standard English Windows folder structure (e.g., `Users`). If your system uses a different language (like `Användare` in Swedish), you will need to update the paths in the script.
> *   **Customize Exclusions:** You **MUST** review and add your personal user folders (like `.vscode`, `.triton`, etc.) to the `exclude_dirs` list to prevent the script from moving important application files.
> *   **Backup First:** Always have a backup of your important data before running any script that modifies files.
>
> **If you have any doubts, the safer solution is to proactively manage future generations with our cloud-saving nodes, which you can find on our [Patreon](https://www.patreon.com/creepybits).**
