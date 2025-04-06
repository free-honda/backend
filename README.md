# 📦 プロジェクト概要
このプロジェクトは、Python アプリケーションを Docker 上で簡単に実行・開発できる環境を構築しています。
`Makefile` でコマンドを簡略化し、`docker compose` により複数コンテナの管理も簡単に行えます。

---

## 📁 ディレクトリ構成
```
.
├── app
│   ├── __pycache__             # Python のキャッシュファイル（無視可）
│   ├── main.py                 # アプリケーションのメインスクリプト
│   └── requirements.txt        # Python の依存ライブラリ定義
├── docker-compose.yml          # Docker Compose 設定ファイル
├── Dockerfile                  # Docker イメージビルド定義
└── Makefile                    # 開発用コマンドまとめ
```

---

## 🚀 セットアップ手順
### 1. 環境変数の設定（必要に応じて）
`.env` ファイルなどを使用する場合、`docker-compose.yml` にマウントして管理できます。

### 2. Docker イメージをビルドしてコンテナ起動
```bash
make up
```

### 3. コンテナの起動
```bash
make up-d
```

### 4. コンテナの停止
```bash
make down
```

### 5. コンテナに入る
```bash
make exec
```

---

## 🐍 main.py の実行
以下のコマンドでアプリを手動実行できます：
```bash
docker compose run --rm app python app/main.py
```

---

## 📦 requirements.txt
Python ライブラリのインストールは `requirements.txt` に記述し、Dockerfile でインストールされます。

---

## 🧹 キャッシュファイルについて
`__pycache__` ディレクトリは Python 実行時に自動生成されるもので、基本的に Git 管理や配布には不要です。
`.gitignore` に追加するのがおすすめです。

---

## 🔧 Makefile コマンド例
```Makefile
up:
	docker compose up --build

up-d:
	docker compose up -d

ps:
	docker compose ps

logs:
	docker compose logs

exec app:
	docker exec -it fastapi-app bash

exec db:
	docker exec -it mysql-db bash

down:
	docker compose down
```

---

## 📝 備考
- Python のバージョンは `Dockerfile` 内で指定。
- 複数人での開発やCIにも対応可能な構成です。
- 必要に応じて volume や port の設定を変更してください。

---

## 📬 お問い合わせ
何か質問がある場合は、Issue または Pull Request をご利用ください。

Happy Coding! 🎉

