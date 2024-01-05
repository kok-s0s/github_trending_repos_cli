# GitHub Trending Repositories CLI

![LiCENSE](https://img.shields.io/badge/License-MIT-green?labelColor=blue-green&style=flat) ![Python](https://img.shields.io/badge/Python-blue?style=flat)

A command-line tool for retrieving trending GitHub repositories based on different time periods.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
- [License](#license)

## Features

- Fetch trending repositories from GitHub.
- Filter repositories by programming language.
- Display repository information including name, author, link, description, language, stars, and forks.

## Installation

```bash
pip install github-trending-repos
```

## Usage

```bash
github-trending-repos daily --language python --page 1
```

- `daily`, `weekly`, or `monthly` are the available time periods.
- `--language` allows you to filter repositories by programming language.
- `--page` lets you navigate through different pages of results (0 to 4).

## Options

- **period**: Trending period (`daily`, `weekly`, or `monthly`).
- **language**: Filter repositories by programming language.
- **save**: Save data as JSON (optional).
- **page**: Page index (default: 0).

## Examples

- Retrieve daily trending Python repositories:

  ```bash
  github-trending-repos daily --language python
  ```

- Save weekly trending repositories with JavaScript language to a JSON file:

  ```bash
  github-trending-repos weekly --language javascript --save
  ```

- View the second page of monthly trending repositories:

  ```bash
  github-trending-repos monthly --page 1
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/kok-s0s/github_trending_repos_cli/blob/main/LICENSE) file for details.
