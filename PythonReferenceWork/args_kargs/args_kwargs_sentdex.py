# https://www.youtube.com/watch?v=gZB_ENJD34E

#think of *args as a list, allows you to throw in an unlimite dnumber of arguments
#think of **kwargs as a dictionary (keyword args (key=value))

blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool'
blog_3 = 'Look at my cat'

site_title = "MY BLOG"

#args
def blog_posts(title, *args):
    print(f"The name of my blog is: {title}")
    print("My posts are:")
    for post in args:
        print("\t" + post)

#kwargs
def blog_posts_kw(title, **kwargs):
    print(f"The name of my blog is: {title}")
    print("My posts are:")
    for p_title, post in kwargs.items():
        print(p_title, post)

#args and kwargs
def blog_posts_kw_a(title, *args, **kwargs):
    print(f"The name of my blog is: {title}")

    print("My args are:")
    for arg in args:
        print(arg)

    print("My keyword posts are:")
    for p_title, post in kwargs.items():
        print(p_title, post)


blog_posts(site_title, blog_1, blog_2, blog_3)

print("-------------------------------------------------------------")

blog_posts_kw(site_title, 
                    blog_1='I am so awesome', 
                    blog_2 ='Cars are cool', 
                    blog_3 ='Look at my cat')

print("-------------------------------------------------------------")
blog_posts_kw_a(site_title, '1', '2', 'red',
                    blog_1='I am so awesome', 
                    blog_2 ='Cars are cool', 
                    blog_3 ='Look at my cat')