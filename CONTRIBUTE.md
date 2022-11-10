# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little help, and credit will always be given.

## Environment setup

Nothing easier!

Requires Python 3.7 or above.

!!! todo

    Recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.

Install pyenv

```bash
brew update
```

```bash
brew install pyenv
```

Set up your shell environment for Pyenv

=== "Bash"

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    ```

=== "Zsh"

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    ```

!!! tip

    Then, if you have `~/.profile`, `~/.bash_profile` or `~/.bash_login`, add the commands there as well.

Restart your shell
```bash
exec "$SHELL"
```

Install Python 3.7
```bash
pyenv install 3.7:latest
```

Make it available globally
```bash
pyenv global 3.7
```

!!! todo

    Install <a href="https://python-poetry.org/docs"><code>Poetry</code></a>.

=== "Linux/macOS"

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

=== "Windows"

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

!!! todo

    Install <a href="https://github.com/git-guides/install-git"><code>git</code></a>

!!! tip

    Recommend using <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"><code>SSH</code></a> or <a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"><code>access token</code></a>

Clone the git repository

```
git clone <repository-url>
```

## Tasks (Sessions)

This project uses <a href="https://nox.thea.codes/"><code>nox</code></a> to run tasks (Sessions).
A `noxfile.py` contains all the tasks running under poetry virtual environment.

To list all tasks available in `noxfile.py`
```bash
nox --list
```

## Development

As usual:

1. create a new branch: `git checkout -b feature-or-bugfix-name`
2. edit/write the code and/or the documentation
3. edit/write tests


<div class="center-table" markdown>

| Type                       | Public              | Private                     |
|----------------------------|---------------------|-----------------------------|
| Packages                   | snake_case          |                             |
| Modules                    | snake_case          | _snake_case                 |
| Classes                    | PascalCase          | _PascalCase                 |
| Exceptions                 | PascalCase          |                             |
| Functions                  | snake_case()        | _snake_case()               |
| Global/Class Constants     | SNAKE_CASE_ALL_CAPS | _SNAKE_CASE_ALL_CAPS        |
| Global/Class Variables     | snake_case          | _snake_case__snake_case     |
| Instance Variables         | snake_case          | _snake_case                 |
| Method Names               | snake_case()        | _snake_case()__snake_case() |
| Function/Method Parameters | snake_case          |                             |
| Local Variables            | snake_case          |                             |

</div>

## Before committing
Make sure build passes all standards, specifications,checks and tests.
```bash
poetry shell
```

```bash
poetry install
```

```bash
nox
```

!!! warning

    Recommend to use `nox -s commit` instead of `git commit`
    If you want to use `git commit` then strictly follow our
    `commit message convention`

    `nox -s commit` will automatically bump the version (if required),
    create version tag, update version files and update changelog file

```bash
nox -s commit
```

1. follow our [commit message convention](#commit-message-convention)


Update the [changelog](changelog.md).

## Commit message convention

Commit messages must follow the
<a href="https://www.conventionalcommits.org/"><code>Conventional commits style</code></a>

!!! info

    ```
    <type>[(optional scope)]: <description>
    <BLANK LINE>
    [optional body]
    <BLANK LINE>
    [optional footer]
    ```

Type can be:
- `build`: About packaging, building wheels, etc.

- `chore`: About packaging or repo/files management.

- `ci`: About Continuous Integration.

- `docs`: About documentation.

- `feat`: New feature.

- `fix`: Bug fix.

- `perf`: About performance.

- `refactor`: Changes which are not features nor bug fixes.

- `style`: A change in code style/format.

- `tests`: About tests.

Scope can be:
- `api`: About api.

- `lambda`: About serverless lambda function.

- `apigateway`: About api  gateway.

- `loggroup`: About log group.

**Description (and body) must be valid Markdown.**

**Footer should contain Jira/Ticket reference number and/or Reviewer name**

!!! example

    ```
    fix: prevent racing of requests

    Introduce a request id and a reference to latest request. Dismiss
    incoming responses other than from latest request.

    Remove timeouts which were used to mitigate the racing issue but are
    obsolete now.

    Reviewed-by: John Smith
    Refs: #123, #456
    ```

!!! example

    ```
    docs: correct spelling of CHANGELOG
    ```

!!! attention

    BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:,
    or appends a ! after the type/scope, introduces a breaking API change
    (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part
    of commits of any type.


!!! example

    ```
    feat: allow provided config object to extend other configs

    BREAKING CHANGE: `extends` key in config file is now used for extending other config files
    ```

OR

!!! example

    ```
    feat(api)!: send an email to the customer when a product is shipped
    ```


## Pull requests guidelines

Link to any related issue in the Pull Request message.
Communicate reviewers/testers in Jira and Slack with Jira ticket and PR links
If branch is deployed to sandbox environment, then provide link to access it.

During review, recommend using fixups:
```bash
# SHA is the SHA of the commit you want to fix
git commit --fixup=SHA
```

Once all the changes are approved, you can squash your commits:
```bash
git rebase -i --autosquash branch
```

And push:
```bash
git push
```
