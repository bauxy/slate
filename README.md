# Bauxy Documentation with Slate
Documentation for the Bauxy API, generated using Slate.

## Getting Started with Slate
### Prerequisites
You're going to need:
- **Linux or OS X** -- Windows may work, but is unsupported.
- **Ruby, version 1.9.3 or newer**
- **Bundler** -- If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Getting Set Up
1. Fork this repository on Github.
2. Clone _your forked repository_ (not our original one) to your hard drive with `git clone https://github.com/YOURUSERNAME/slate.git`
3. `cd slate`
4. Initialize and start Slate. You can either do this locally, or with Vagrant:

```shell
# either run this to run locally
bundle install
bundle exec middleman server

# OR run this to run with vagrant
vagrant up
```

You can now see the docs at [http://localhost:4567](http://localhost:4567). Whoa! That was fast!

Now that Slate is all set up your machine, you'll probably want to learn more about [editing Slate markdown](https://github.com/tripit/slate/wiki/Markdown-Syntax), or [how to publish your docs](https://github.com/tripit/slate/wiki/Deploying-Slate).

If you'd prefer to use Docker, instructions are available [in the wiki](https://github.com/tripit/slate/wiki/Docker).

## Need Help? Found a bug?
Read our [contribution guidelines](https://github.com/tripit/slate/blob/master/CONTRIBUTING.md), and then [submit an issue](https://github.com/tripit/slate/issues) to the Slate Github if you need any help. And, of course, feel free to submit pull requests with bug fixes or changes.
