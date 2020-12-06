# Opportunity Cell Website

## Important Info

### Markdown syntax

All front matter is written in Markdown.

[This page](https://guides.github.com/features/mastering-markdown/) has further instruction. This is so that editing the front matter is easy and does not require expert understanding of html.

### Page variables

At the start of `*.md` files, there will be a section delimited by `---`. These are variables for each page.

1. `title` - title of the page
2. `nav_title`\[Optional\] - the text to be used in the navbar. `title` used as default
3. `nav_index` - the position of the page in the navbar. Sorted alphabetically otherwise.
4. `nav_ignore` - set to `true` if page is not to be shown in the navbar.
5. Other default variables can be found [here](https://jekyllrb.com/docs/variables/#page-variables)

### baseurl variable in config.yaml

Set the `baseurl` variable in `config.yaml` according to wherever you are going to host this site from relative to the root. For example, if the website is to be hosted on `https://web.iisermohali.ac.in/students/oppcell`, then set `baseurl: "/students/oppcell"`.
If viewing on Github, comment out the line as `# baseurl: ...`

## Updating and Publishing

### Ubuntu

1. Download/clone this repo, or one of the releases
2. cd to the downloaded repo.
3. Run `bash ./preinstall`. It will install Ruby, and the Jekyll and Bundler gems and initialize the gems. If you prefer to install them yourself, go to [Others](#others). You can skip certain steps if you have already performed them before.
4. Run `bundle exec jekyll serve`
5. Open the browser to the server address as outputted in the previous command.
6. You should be able to see the site. Make changes as necessary, and check using `bundle exec jekyll serve`.
7. **When you are happy, use the files generated in `_site` and place in the production server.** Make sure you have set the `baseurl` in `_config.yaml` as discussed in [Important Info](#important-info).
8. Make sure you update `README.md` if necessary.
9. Done!

### Others

1. Follow the steps as described in the [Jekyll installation page](https://jekyllrb.com/docs/installation/)
2. cd to the repo
3. Run `bundle install` then, `bundle update`
4. Continue with Step 4 of [Ubuntu instructions](#ubuntu)
