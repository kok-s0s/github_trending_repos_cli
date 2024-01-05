#!/usr/bin/env python3

import requests
import json
import argparse
import sys
from bs4 import BeautifulSoup
from pytermgui import tim


def get_trending_repositories(period, language=None, save_data=False):
    base_url = "https://github.com/trending"
    url = f"{base_url}?since={period}&spoken_language_code="
    if language:
        url = f"{base_url}/{language}?since={period}&spoken_language_code="

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        repos_data = []

        repos = soup.find_all("article", class_="Box-row")
        for repo in repos:
            [author, repo_name] = (
                repo.find("h2", class_="h3 lh-condensed").text.strip().split("/")
            )
            link = repo.find("h2", class_="h3 lh-condensed").find("a")["href"]
            description_element = repo.find(
                "p", class_="col-9 color-fg-muted my-1 pr-4"
            )
            description = (
                description_element.text.strip() if description_element else None
            )
            programming_language_element = repo.find(
                "span", class_="d-inline-block ml-0 mr-3"
            )
            programming_language = (
                programming_language_element.text.strip()
                if programming_language_element
                else None
            )
            [stars, forks] = repo.find_all(
                "a", class_="Link Link--muted d-inline-block mr-3"
            )

            repo_data = {
                "author": author.strip(),
                "repo_name": repo_name.strip(),
                "link": f"https://github.com{link}",
                "description": description,
                "programming_language": programming_language,
                "stars": stars.text.strip(),
                "forks": forks.text.strip(),
            }

            repos_data.append(repo_data)

        if save_data:
            output_data = {"period": period, "language": language, "repos": repos_data}
            output_filename = (
                f"trending_repos_{period}_{language}.json"
                if language
                else f"trending_repos_{period}.json"
            )

            with open(output_filename, "w") as json_file:
                json.dump(output_data, json_file, indent=2)

        return repos_data
    else:
        sys.exit(f"Failed to retrieve data. Status code: {response.status_code}")


def repo_card(repo):
    tim.print(
        f"[!gradient(210) italic]Repository: {repo['author']}/{repo['repo_name']}"
    )
    tim.print(f"[!gradient(210) italic]Link: {repo['link']}")
    if repo["description"] != None:
        tim.print(f"[!gradient(210) italic]Description: {repo['description']}")
    if repo["programming_language"] != None:
        tim.print(
            f"[!gradient(210) italic]Language: {repo['programming_language']} Stars: {repo['stars']} Forks: {repo['forks']}"
        )
    else:
        tim.print(
            f"[!gradient(210) italic]Stars: {repo['stars']} Forks: {repo['forks']}"
        )
    tim.print()


def main():
    parser = argparse.ArgumentParser(description="Get trending repositories on GitHub.")
    parser.add_argument(
        "period", choices=["daily", "weekly", "monthly"], help="Trending period"
    )
    parser.add_argument("--language", help="Filter repositories by language")
    parser.add_argument(
        "--save", action="store_true", help="Save data as JSON (optional)"
    )
    parser.add_argument("--page", type=int, default=0, help="Page index (default: 0)")
    args = parser.parse_args()

    period = args.period
    language = args.language
    save_data = args.save
    page_idx = args.page

    repos_data = get_trending_repositories(period, language, save_data)

    if 0 <= page_idx < len(repos_data) // 5:
        tim.print(
            f"[!gradient(210) italic]Trending Repositories ({period}) - page {page_idx}\n"
        )

        start_idx = page_idx * 5
        end_idx = start_idx + 5
        page_data = repos_data[start_idx:end_idx]
        for repo in page_data:
            repo_card(repo)
    else:
        sys.exit("Error: Invalid page index. Please enter a number between 0 and 4.")


if __name__ == "__main__":
    main()
