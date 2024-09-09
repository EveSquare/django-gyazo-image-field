class GyazoImageFile:
    # {
    #     "type": 画像形式,           // png, jpg, gifなど
    #     "thumb_url": サムネールパス, // https://~~~~.png
    #     "created_at": 生成日時,     // 例: 2021-09-09T09:33:35+0000
    #     "image_id": ユニークID,
    #     "permalink_url": Gyazoページのリンク, // 例 : https://gyazo.com/ユニークID
    #     "url": 画像リンク // https://i.gyazo.com/ユニークID.png
    # }

    def __init__(
        self,
        type: str,
        thumb_url: str,
        created_at: str,
        image_id: str,
        permalink_url: str,
        url: str,
    ):
        self.type = type
        self.thumb_url = thumb_url
        self.created_at = created_at
        self.image_id = image_id
        self.permalink_url = permalink_url
        self.url = url
