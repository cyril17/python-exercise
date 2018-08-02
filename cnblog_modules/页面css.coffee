#home {
    margin: 0 auto;
    width: 80%;/*原始65*/
    min-width: 980px;/*页面顶部的宽度*/
    background-color: rgba(245, 245, 245, 0.7);
    padding: 30px;
    margin-top: 50px;
    margin-bottom: 50px;
    box-shadow: 0 2px 6px rgba(100, 100, 100, 0.3);
}
body {
    background: rgba(12, 100, 129, 1) url('http://images.cnblogs.com/cnblogs_com/cyril365/1253002/o_o_124.jpg') fixed no-repeat;
    background-position: 50% 5%;
    background-size: cover;
}
#blogTitle {
    height: 100px;  /*高度*/
    clear: both;
    background-color: rgba(245, 245, 245, 0);
}
#blogTitle h1 {
    font-size: 36px;
    font-weight: bold;
    line-height: 1.8em;/*原始 1.6em*/
    margin-top: 10px;/*原始 15px */
    color: #548B54;
}
#blogTitle h2 {
    font-weight: normal;
    font-size: 17px;/*原始 16px ；font-size: 1.0rem;*/
    line-height: 1.8;
    color: #111;
    font-weight: bold;
    text-align: right;
    float: right;
}
#navigator{
    background-color: rgba(33, 160, 139, 0.9);
}
#navList a:link, #navList a:visited, #navList a:active{
    color: #eee;
    font-size: 18px;
    font-weight: bold;
}
.blogStats{
    color: #eee;
}
.postTitle {
    border-left: 8px solid rgba(33, 160, 139, 0.68);
    margin-left: 10px;
    margin-bottom: 10px;
    font-size: 20px;
    float: right;
    width: 100%;
    clear: both;
}
.postTitle a:link, .postTitle a:visited, .postTitle a:active {
    color: #21759b;
    transition: all 0.4s linear 0s;
}
.postTitle a:hover {
    margin-left: 30px;
    color: #0f3647;
    text-decoration: none;
}
.postCon {
    float: right;
    line-height: 1.5em;
    width: 100%;
    clear: both;
    padding: 10px 0;
}

.day .postTitle a {
    padding-left: 10px;
}
.day {
    background: rgba(255, 255, 255, 0.5);
}
/*文章附加信息*/
.postDesc {
    background: url(images/posted_time.png) no-repeat 0 1px;
    color: #757575;
    float: left;
    width: 100%;
    clear: both;
    text-align: left;
    font-family: "微软雅黑" , "宋体" , "黑体" ,Arial;
    font-size: 13px;
    padding-right: 20px;/*5px  padding-left: 90px;posted 发表时间左边距离*/
    margin-top: 20px;
    line-height: 1.8;
    padding-bottom: 35px;
}

.newsItem, .catListEssay, .catListLink, .catListNoteBook, .catListTag, .catListPostCategory,
.catListPostArchive, .catListImageCategory, .catListArticleArchive, .catListView,
.catListFeedback, .mySearch, .catListComment, .catListBlogRank, .catList, .catListArticleCategory ,#blog-calendar
{
    background: rgba(255, 255, 255, 0.5);
    margin-bottom: 35px;
    word-wrap: break-word;
}

.CalTitle{
    background: rgba(255, 255, 255, 0);
}
.catListTitle{
    background-color: rgba(33, 160, 139, 0.9);
}

#topics{
    background: rgba(255, 255, 255, 0.5);
}

.c_ad_block{
    display: none;
}

#tbCommentBody{
    width: 100%;
    height: 200px;
    background: rgba(255, 255, 255, 0.5);
}

#q{background: rgba(255, 255, 255, 0);}

.CalNextPrev{background: rgba(255, 255, 255, 0);}

.cnblogs_code{
    background: rgba(255, 255, 255, 0);
}

.cnblogs_code div{
    background: rgba(255, 255, 255, 0);
}

.cnblogs_code_toolbar{
    background: rgba(255, 255, 255, 0);
}

.entrylist{
    background: rgba(255, 255, 255, 0.5);
}