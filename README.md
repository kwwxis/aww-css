CSS theme for /r/aww
====================

Images in Use
-------------

  - assets/inherit/snoo.png (upload to both stylesheet and sub settings)
  - assets/awwlogo.png
  - assets/awwbanner.png
  - assets/spritesheet.png
  - assets/commentrules.png
  - assets/nothing-here.png
  - assets/inherit/kitteh.png
  
Installation instructions
-------------------------------

  1. See the "Images in use" section above, upload all these images to the stylesheet page
  
    - no need to change anything in "new image name"
    - assets/inherit/snoo.png should be uploaded to **both** the stylesheet page and the
      "upload header image" section under "look and feel" in the subreddit settings
      
  2. See the "sub/" folder, upload the contents of "sidebar_text.txt", "submission_text.txt", "wiki_index.txt"
     to their respective locations
      
  3. **dist/dist.css** - upload to the stylesheet page
  
Order of Concatenation
----------------------
             
| File name     | Purpose                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------- |
| etc.css       | general layout, common margins, and whatever can't be categorized into the other files                |
| forms.css     | forms other than the submit post form                                                                 |
| submit.css    | submit post form                                                                                      |
| header.css    | subreddit header                                                                                      |
| sidebar.css   | subreddit sidebar (except md and titlebox - sidemd.css and titlebox.css respectively)                 |
| sidemd.css    | sidebar usertext md sections                                                                          |
| titlebox.css  | everything in the sidebar titlebox except for usertext md                                             |
| thing.css     | style for .thing elements common to both links and comments                                           |
| links.css     | linklisting links and page                                                                            |
| linkbtn.css   | link buttons                                                                                          |
| cpage.css     | comments page page layout & top area (panestack-title, menuarea)                                      |
| ctable.css    | sitetable and comments in comments page                                                               |
| usertext.css  | usertext editor and common md styles                                                                  |
| search.css    | search page (does not include search input in sidebar - sidebar.css)                                  |
| footer.css    | subreddit footer                                                                                      |
| wiki.css      | subreddit wiki                                                                                        |
| modpages.css  | any moderator pages that required additional CSS                                                      |
| ext.css       | misc. styles for extensions (RES, Mod Toolbox, etc.) that can't be categorized into the other files   |
| temp.css      | temporary                                                                                             |
| nightmode.css | nightmode                                                                                             |
| media.css     | extra media queries for small screens and such                                                        |