from feedformatter  import Feed
import time

# Create the feed
feed = Feed()

# Set the feed/channel level properties
feed.feed["title"] = "Example feed"
feed.feed["link"] = "http://www.example.com"
feed.feed["author"] = "Mr X. Ample"
feed.feed["description"] = "A simple example feed with one item in it"

# Create an item
item = {}
item["title"] = "Test item"
item["link"] = "http://www.example.com/example_url"
item["description"] = "And now for something completely different"
item["pubDate"] = time.localtime()
item["guid"] = "1234567890"

# Add item to feed
# You can do this as many times as you like with multiple items
feed.items.append(item)

# Print the feed to stdout in various formats
print feed.format_rss1_string()
print feed.format_rss2_string()
print feed.format_atom_string()

# Save the feed to a file in various formats
feed.format_rss1_file("example_feed_rss1.xml")
feed.format_rss2_file("example_feed_rss2.xml")
feed.format_atom_file("example_feed_atom.xml")
