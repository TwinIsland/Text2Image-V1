![something under this photo](https://cdn-1257758577.cos.ap-chengdu.myqcloud.com/2019/06/21/1561107190.png)

------

## Usage

**text to photo:**

- `cd` to the program folder
- put the photo you wanna convert as `input.jpg` and the text as `input.txt` in the folder
- then, run `python wtp.py`
- the `output.png` will be the result

**photo to text:**

- make sure `output.png` is in the folder
- then, run `python wtp.solver.py` 
- and the `output.txt` will be the result

## Principle

- For the `rgb` layer in a photo, the less sensitive layer is `b` which means if you modified the `b` layer, the change of the photo is the smallest. Therefore, my first step is to convert the photo’s whole `b` layer’s data into even number, so that I can memorize  binary data inside

- To convert String to Binary, it is not just using `bin(int(ord(string),10)` because if we only use this method, many spacing will leaved, like: `101011 101111 101001`, and of course, our input photo does not support this format  

- So, I think some ways to try to solve this, which is to use a way to convert the string, no matter what is its `ascill` to a pure binary sequence without spacing, at the same time, I also need to make the data loss relatively low. Finally, I think of a solution which is to use the `pointer` value and `navigator` value to represent the position of the data. 

![50483-2larwtk8t1u.png](https://cdn-1257758577.cos.ap-chengdu.myqcloud.com/2019/06/21/1561107253.png)
  `Navigator value`: to show the length of the index pointer

  `index pointer`: to show the length the of the index navigator

  `index navigator`: to show the length of each data

  `data`: binary information for each string’s `ascill`

  It is true that it will create many data loss:  $L(x) = 2x + 3$. But I cannot think of a better way, plus I do not have enough time. Therefore, If you have a better solution, please tell me.

  there are many details I do not mention in this doc, like why each `index navigator` are all composed in 5 elements, and why there are two `navigator values`, but not one... If you want to know more. contact me by [email](mailto://p@hty.email).

## demo
the first photo of this post

## open source
in my [gitlab](https://gitlab.com/wyatthuang)
or download: [here](https://gitlab.com/wyatthuang/wtp/-/archive/master/wtp-master.zip)

