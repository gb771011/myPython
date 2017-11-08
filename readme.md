# Index
* [基本語法](./syntax.md)

# Reference
[YT-周莫烦](https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg)
[菜鳥教程](http://www.runoob.com/python3/python3-basic-operators.html)

# vscode設定
## pylint-關閉不必要的警告
vsc的預設python語法檢查工具是pylint，但是會常常出現一些不太重要的警告，可以在vsc的工作區設定中關掉它
* 設定pylint的引數
    1. 開啟設定( **Ctrl+,** )
    1. 切換到工作區設定(可略)
    1. 在左側的設定中搜尋 **python.linting.pylintArgs** 這個選項，並複製到右側的工作區設定中
    1. 在**python.linting.pylintArgs**中填入`"disable=C0103"`，或將_C0103_換成其他的Id即可
    1. 每一條項目就要打一次`"disable=X0000"`，若想要關閉的項目的不多時可以這樣做

* 在.pylintrc中設定(類似JS的.eslintrc)
    1. 在CMD輸入下列指令將所有的資訊存到pylintlistmsg.txt
        ```
        pylint --list-msg > pylintlistmsg.txt
        ```
    1. 開啟pylintlistmsg.txt，並找到要關閉的警告名稱為何
    1. 同樣在cmd中輸入下列指令以建立pylint的設定檔`.pylintrc`
        ```
        pylint --genarate-rcfile --rcfile=.pylintrc
        ```
        引數說明:
        * --generate-rcfile: 建立設定檔案，若在vscode中的cmd建立的話，檔案會自動存放在工作區下
        * --rcfile=.pylintrc: 設定檔名，之後的設定還會用到，請注意
    1. 在vscode中開啟.pylintrc，並在右下角設定語言模式為`Properties`(主要是為了方便檢視)
    1. 在.pylintrc找到`disable`參數，並在現有的值之後加上剛剛查到的名稱即可(記得加逗號)

    建立設定檔案的好處是可以針對其他項目做進一步的設定，但注意，一旦pylint有在工作區找到設定檔案，之後在該工作區下使用cmd操作pylint時就會自動導入設定檔案&檢查

---
