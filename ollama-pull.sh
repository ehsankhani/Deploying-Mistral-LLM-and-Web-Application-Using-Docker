#!/bin/bash
echo "Starting server"
ollama serve &
sleep 1
echo "Pulling mistral"
ollama pull mistral 