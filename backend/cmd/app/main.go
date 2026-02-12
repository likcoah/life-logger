package main


import (
	"log"
	"os"
	"os/signal"
	"syscall"
	"context"
	"github.com/likcoah/life-logger/internal/bot"
)


func main() {
	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer cancel()

	token := os.Getenv("BOT_TOKEN")
	if token == "" {
		log.Fatal("Token not set")
	}

	tgBot, err := bot.New(token)
	if err != nil {
		log.Fatalf("Bot initialization error: %v", err)
	}

	tgBot.Start(ctx)
}

