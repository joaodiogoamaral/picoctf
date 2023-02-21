

In this challenge, the first thing I did was to examine the page source code (Inspect menu on Chrome/Brave).

Inside the HTML code, I could see the following comment:

`<!-- Here's the first part of the flag: picoCTF{t -->`

Then I snooped around a bit more, exploring the JavaScript sources (sources tab in teh Inspect Element window), where i found the next portion in the CSS file:


`/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */`

Continuing, I decided to check the common files which are included in the website, like [Robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro), in http://mercury.picoctf.net:5080/robots.txt,
the contents of that file were:

`User-agent: *`
 Disallow: /index.html`
`Part 3: t_0f_pl4c`
`I think this is an apache server... can you Access the next flag? `


This part also provided a hint, so I googled for "common apache server files" (actually did many searches along these lines), and I stumbled on the [.htaccess](https://httpd.apache.org/docs/2.4/howto/htaccess.html) file, which is used to store some apache configurations. Checking that file by accessing http://mercury.picoctf.net:5080/.htaccess.

`# Part 4: 3s_2_lO0k`
`# I love making websites on my Mac, I can Store a lot of information there.`

Looks like this portion also contains a hint, following the same reasoning as in the previous step, I googled for "common MACOS files" and one of those files is the [DS_Store](https://buildthis.com/ds_store-files-and-why-you-should-know-about-them/) file. So I checked in http://mercury.picoctf.net:5080/.DS_Store:

`Congrats! You completed the scavenger hunt. Part 5: _35844447}`


And that's all, Folks!

*Flag: picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}*
