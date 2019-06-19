SlackのOutgoing Webhookと組み合わせてIAMキーの有効/無効を切り替えるSlackコマンドを作成。

# 準備

```bash
npm ci

# 環境変数設定 
cp .envrc.sample .envrc
direnv edit
```

# デプロイ

```bash
npm run deploy
```

## プロダクション環境

```bash
yarn deploy:production
```

