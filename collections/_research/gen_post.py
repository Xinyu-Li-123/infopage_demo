# Generate posts to test tag system

import os 
import numpy as np

template = """---
layout: post
title:  "{title}"
subtitle: "{subtitle}"
date:   {date}
tags: {tags}
author: {author}
---
{content}
"""

num_post = 6
# generate random, meaningful tags
all_tags = ['Frontend', 'Backend', 'HTML', 'CSS', 'JavaScript', 'Python', 'C', 'C++', 'Java', 'Computer Network', 'Operating System', 'Distributed System', 'Deep Learning', 'Life', 'Void']
all_authors = ['James Adam', 'RandomHumanBeing123', 'Mike Dane', 'Lorep Ipsum']

try:
    os.chdir('_posts')
except FileNotFoundError:
    pass

for i in range(num_post):
    title = "Post " + str(i)
    subtitle = "Subtitle " + str(i)
    date = "2021-{}-{}".format(3+i//30, 1+i%30)
    tags = np.random.choice(all_tags, size=np.random.randint(2, 6), replace=False)
    tags = ['"' + tag + '"' for tag in tags]
    tags = '[' + ', '.join(tags) + ']'
    author = np.random.choice(all_authors)
    content = "This is a post " + str(i)
    post = template.format(
        title=title, 
        subtitle=subtitle, 
        date=date, 
        tags=tags, 
        author=author,
        content=content)
    filename = f"{date}-post-" + str(i) + ".md"
    with open(filename, 'w') as f:
        f.write(post)