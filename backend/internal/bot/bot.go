package bot


import (
	"log"
	"context"
	"github.com/go-telegram/bot"
	"github.com/go-telegram/bot/models"
)


type Bot struct {
	client	*bot.Bot
}


func New(token string) (*Bot, error) {
	b := &Bot{}

	opts := []bot.Option{
		bot.WithDefaultHandler(b.defaultHandler),
	}

	tg, err := bot.New(token, opts...)
	if err != nil {
		return nil, err
	}

	tg.RegisterHandler(bot.HandlerTypeMessageText, "/start", bot.MatchTypeExact, b.startHandler)

	b.client = tg
	return b, nil
}


func (b *Bot) defaultHandler(ctx context.Context, b_tg *bot.Bot, update *models.Update) {
	if update.Message == nil || update.Message.Text == "" {
		return
	}

	b_tg.SendMessage(ctx, &bot.SendMessageParams{
		ChatID: update.Message.Chat.ID,
		Text: update.Message.Text,
	})
}


func (b *Bot) startHandler(ctx context.Context, b_tg *bot.Bot, update *models.Update) {
	b_tg.SendMessage(ctx, &bot.SendMessageParams{
		ChatID: update.Message.Chat.ID,
		Text: "Hi, " + update.Message.From.FirstName,
	})
}


func (b *Bot) Start(ctx context.Context) {
	log.Print("Bot started")
	b.client.Start(ctx)
	log.Print("Bot stopped")
}

