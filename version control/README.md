# Version Control

_Source Control_
The practice of managing code through versions. It is a way to track and manage changes made to a codebase. Historical changes are kept to allow earlier versions to be recovered.

## Centralized Version Control

The codebase exists in a developer's computer, while the full version history resides on a central server.

**Examples:** **`CVS (Concurrent Versions System)`**, **`SVN (Subversion)`**

## Distributed Version Control

Is a system in which the codebase is mirrored on every developer's computer. Full version history and file changes are available to all. While it may seem less space-efficient to store full version history on a everybody's computer, it is not a problem as nowadays storage space is so cheap. Plus, source code is usually just plain text, with the exception of assets such as images, font files, and other media.

**Examples:** **`Git`**, **`Mercurial`**

## Repositories

Are the stores in which code is hosted. You can update repositories from multiple clients at once. Repositories are often viewable to the public eye. Even if they are marked private, it is crucial to **keep sensitive information away from source control** platforms.

### What to ignore

Any sensitive information, such as secret keys used in encryption, or API keys, should be stored as environment variables on the system hosting your web application. Never push these to any version control system. Moreover, compilation output, such as .exe files or .out does not need to be included either. Each developer can compile the source code on their machine.
