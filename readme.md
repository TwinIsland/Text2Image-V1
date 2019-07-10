![something under this photo](https://cdn-1257758577.cos.ap-chengdu.myqcloud.com/2019/06/21/1561107190.png)

By using this tool, you can easily hide your text in your picture.

------

# Usage

**text to photo:**

- `cd` to the program folder
- put the photo you wanna convert as `input.jpg` and the text as `input.txt` in the folder
- then, run `python wtp.py`
- the `output.png` will be the result

**photo to text:**

- make sure `output.png` is in the folder
- then, run `python wtp.solver.py` 
- and the `output.txt` will be the result

# Principle

- For the `rgb` layer in a photo, the less sensitive layer is `b` which means if you modified the `b` layer, the change of the photo is the smallest. Therefore, my first step is to convert the photo’s whole `b` layer’s data into even number, so that I can memorize  binary data inside

- To convert String to Binary, it is not just using `bin(int(ord(string),10)` because if we only use this method, many spacing will leaved, like: `101011 101111 101001`, and of course, our input photo does not support this format  

- So, I think some ways to try to solve this, which is to use a way to convert the string, no matter what is its `ascill` to a pure binary sequence without spacing, at the same time, I also need to make the data loss relatively low. Finally, I think of a solution which is to use the `pointer` value and `navigator` value to represent the position of the data. 

![27052-lzzjpztw8re.png](https://cdn-1257758577.cos.ap-chengdu.myqcloud.com/2019/06/30/1561862804.png)

  `Navigator value`: to show the length of the index pointer

  `index pointer`: to show the length the of the index navigator

  `index navigator`: to show the length of each data

  `data`: binary information for each string’s `ascill`

  It is true that it will create many data loss:  $L(x) = 2x + 2$. But I cannot think of a better way, plus I do not have enough time. Therefore, If you have a better solution, please tell me.

  there are many details I do not mention in this doc, like why each `index navigator` are all composed in 5 elements, and why there are two `navigator values`, but not one... If you want to know more, plz remind me by commenting.

# A better solution
![23107-8dzajqn5k3.png](https://cdn-1257758577.cos.ap-chengdu.myqcloud.com/2019/06/30/1561862395.png)

Yesterday, when I figure out a much better solution to transfer the data to continue binary when I was dreamming, and theoretically, the **Max storage in photo** reach $Max(storage) = \frac{(h*w)-4}{Max(len(data))}$ where `len` there represent the length of each data, and the **max possible storage** is: $\frac{\sum_i^{u=30}2^i}{Max(len(data))}$, which means that for a **4k** picture, and all the parameter is written in English, the max number of word the photo can storage is: $\frac{3068*1068-4}{6} = 546103$.

# demo
the first photo of this post

# open source
in my [gitlab](https://gitlab.com/wyatthuang)
or download: [here](https://gitlab.com/wyatthuang/wtp/-/archive/master/wtp-master.zip)