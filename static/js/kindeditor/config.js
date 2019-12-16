KindEditor.ready(function (k) {
    window.editor = k.create('textarea[name="content"]',{    //这个地方需要注意；模型类中使用 text = models.TextField()的话id就是id_text。如果是提前字段类型可以到浏览器中检查，获取到需要使用富文本编辑器的元素的id
            allowImageRemote: true,
            allowImageUpload: true,
            allowFileManager: true,
        uploadJson : '/upload/kindeditor/', //这个是上传图片后台处理的url
        extraFileUploadParams: {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
            },
         filePostName: 'imgFile',
        width:'1400px',
        height:'700px',
    });
})