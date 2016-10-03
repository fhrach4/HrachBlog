Title: The Thoughtfulness of Windows Phone 8.1
Date: 2016-9-29
Category: Tech
tags: 30 Day Challenge, Mobile
Author: Frank Hrach


In my previous post, I mentioned that the best phone I had ever owned was the Nokia Lumia 920. While the hardware
was excellent, a large part of my fondness for the device is due to its operating system: Windows 8.1 Mobile.
Windows phone is the butt of many jokes, but really, the other two contenders in the mobile OS space could learn a
lot from some of the design choices of Windows Phone.


### Multitasking
One of the things Windows phone does exceptionally well is handling multiple applications running at once. Each
application runs in a sandbox, not unlike a docker container. This allows the phone to easily "hibernate" an
application when it is sent to the background, instead of the phone trying to run every application all at once,
and closing them when resources are needed. This model, however, does not allow for background tasks as only one
application can be "awake" and running at a time. This is solved by applications being able to register a
*background service* which can always run even when the application is not in the foreground. These use fewer
resources than the main application, and the user can allow or disallow any application from running in the
background if they wish. The advantage of this system, is even very-low end phones don't suffer performance
penalties from having many applications open, and, it enables the user to have more control over their battery life
as no service can run by accident in the background.


### Calendar and Mail
One of the most useful features of Windows Phone was how it handled email. Call me old fashioned, but 99% of my
phone's use time is dealing with calendar and email. The way Windows Phone handled these wasn't too different from
many competitors: you simply registered your account with the operating system, and applications could ask for the
main update service to retrieve information from the accounts based off of a permission system. Applications could,
of course, store and authenticate with their own set of credentials not managed by the operating system, but for
any services from Google, Microsoft, Amazon, etc. it was much more convenient to use the credential store since the
account was most likely going to be used in multiple applications. The key difference with Windows Phone was the
sheer number of third-party accounts this worked with. This is most likely only because Windows Pone never managed
to get above 7% of the US smartphone market share, so they had to accommodate as many platforms as possible instead
of being able to leverage their position to force everyone to use their platform.

Because the operating system handles account authentication for mail, that means that the operating system itself
can manage reminders and mail tasks. This has several advantages: you are not blindly trusting a third-party
application with your login information, and, it lets the OS take actions to optimize various aspects. The first
part is self-explanatory, since the application never directly sees your username and password, a malicious
application can not take the information. The latter tends to be rather silent but useful: the operating system can
change the frequency that an account is updated, and thus saving power, dynamically based off of usage.


### Music
Somehow, the secondary function of my phone is not to take calls, it's to play music, and Windows Phone set the
standard I use for judging media controls. Playing music works like any other device, naturally, but the controls
are all placed in logical and thoughtful places. For example, as soon as a background task playing music is
registered, the lock-screen is replaced with fully functional media controls. These are much easier to use than
other smartphones I've used since the entire lock-screen changes to accommodate the new primary task, instead of
placing a small set of controls. The other incredibly useful feature is that a minimal set of controls (next,
previous, and play/pause) appears on the volume screen. When the volume button is pressed up or down, a card slides
down from the top of the screen. When music is playing, the controls are added to that menu. This enables the user
to pause their music or skip a song they don't like even while in a different application.



Overall, there are quite a few very well though out aspects of Windows Phone as a platform. It appears that the
platform will not survive five more years in the current market, but perhaps some of these design choices can come
to other platforms.
