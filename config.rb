require 'digest'
require 'base64'

# Markdown
set :markdown_engine, :redcarpet
set :markdown,
    fenced_code_blocks: true,
    smartypants: true,
    disable_indented_code_blocks: true,
    prettify: true,
    tables: true,
    with_toc_data: true,
    no_intra_emphasis: true

# Assets
set :css_dir, 'stylesheets'
set :js_dir, 'javascripts'
set :images_dir, 'images'
set :fonts_dir, 'fonts'

# Activate the syntax highlighter
activate :syntax

activate :autoprefixer do |config|
  config.browsers = ['last 2 version', 'Firefox ESR']
  config.cascade  = false
  config.inline   = true
end

# Github pages require relative links
activate :relative_assets
set :relative_links, true

# Build Configuration
configure :build do
  # If you're having trouble with Middleman hanging, commenting
  # out the following two lines has been known to help
  activate :minify_css
  activate :minify_javascript
  # activate :relative_assets
  # activate :asset_hash
  # activate :gzip
end

helpers do
  def docstring(path, method, rebuild_cache=true)
    file = File.open(path)
    contents = file.read

    # Get Docstring
    docstring_regex = /def #{method}\([^\)]*\):\s*"""([\s\S]*?)"""/
    match = contents.match(docstring_regex)
    return '' unless match
    docstring = match[1]

    # Clean Docstring
    # Close to https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
    lines = docstring.gsub(/\t/,"    ").lines().map{|a| a.rstrip}
    indent = lines
      .reject {|a| a.match(/^\s*$/)}
      .map {|a| a.length - a.lstrip.length}
      .min
    lines.map! do |a|
      amount = [indent, a.match(/^( *)/)[1].length].min
      a[amount..-1]
    end
    cleaned_docstring = lines.join("\n")

    # Expand shell commands
    cleaned_docstring.gsub(/^ *\$ .+$/) do |match|
      cmd = match.match(/\$ (.+)$/)[1]
      if build?
        cmd_hash = Digest::SHA256.hexdigest(cmd)[0..20] 
        b64_path = Base64.encode64(path)
        cache_name = "#{b64_path}-#{method}-#{cmd_hash}"
        cache_filepath = "./source/cache/#{cache_name}.md"

        if rebuild_cache?
          output = `#{cmd}`
          md_output = "```sh\n$ #{cmd}\n\n#{output}\n```"
          # save to cache and return
          File.write(cache_filepath, md_output)
          md_output
        else
          # read cache
          File.read(cache_filepath)
        end
      else
        "```sh\n$ #{cmd}\n\n<Output from the above command will go here on build>\n```"
      end
    end
  end
end
