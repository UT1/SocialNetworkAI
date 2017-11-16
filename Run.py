from Wit_Speech_to_text import *
from speech2 import *
from Crawler import *
from Twitter_bot import *

print "****************************Social Network AI**********************************\nInitiating Bot....";

print "Initiating Twitter Application.......\n******Menu******\n1.Post a Tweet\n2.Send a direct message\nEnter your choice:";
x=(int)(raw_input());
if x==1:
    print "Options Available:\n1.Post a quote\n2.Post a Voice to text tweet\n3.Post on your own";
    ch=(int)(raw_input());
    if ch==1:
        print "How are you feeling right now??\nSay....";
        rec=Recorder();
        rec.record_it();
        ct=Speech_to_text();
        sj=ct.convert();
        text_from_speech=str(sj['_text']);
        # print text_from_speech;
        s=MyQuery();
        qu=s.quote('rain');
        print "The quote extracted is:"+qu;
        gh=twitter_bot();
        gh.send_tweet(qu);
        print "Posted Succesfully";
    if ch==2:
        print "Say the quote....";
        rec=Recorder();
        rec.record_it();
        ct=Speech_to_text();
        sj=ct.convert();
        text_from_speech=str(sj['_text']);
        gh=twitter_bot();
        gh.send_tweet(text_from_speech);
        print "Posted Succesfully";
    if ch==3:
        print "Enter the tweet:";
        tw=raw_input();
        gh=twitter_bot();
        gh.send_tweet(tw);
        print "Posted Succesfully";

else :
     print "Options Available:\n1.Send a simple Message\n2.Send a Voice to text message";
     ch=(int)(raw_input());
     if ch==1:
         s=twitter_bot();
         print "Enter the message:"
         message=raw_input();
         s.send_message(message);
         print "Message Sent Succesfully";
     if ch==2:
        print "Say the message....";
        rec=Recorder();
        rec.record_it();
        ct=Speech_to_text();
        sj=ct.convert();
        text_from_speech=str(sj['_text']);
        gh=twitter_bot();
        gh.send_message(text_from_speech);
