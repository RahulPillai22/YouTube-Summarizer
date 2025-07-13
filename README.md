# YouTube-Summarizer
A modern, modular multi-agent system that takes a user's prompt, searches for a relevant YouTube video, transcribes it, summarizes the content using LLMs (Gemini), and outputs a reviewed and polished summary in a formatted PDF.

## 🔍 Project Overview

This project demonstrates how to build an intelligent multi-agent workflow using cutting-edge tools like LangGraph, Google Gemini 2.5 Pro, and the YouTube Search & Transcript APIs. Each agent in the system handles a specialised task, forming a pipeline from input to a structured PDF summary.

## 👤 Use Case

Given a user query like:

"Video on Korea by Kurzgesagt"

The system:

> - Uses Gemini to interpret the query
>
> - Fetches the most relevant YouTube video
>
> - Retrieves and summarizes the transcript
>
> - Reviews and polishes the summary
>
> - Outputs it into a professional PDF document

## 🚀 Features

- LLM-based summarization and review

- Automated video discovery and transcription

- PDF output with clean formatting

- Stateful, modular agent design

- Built on LangGraph with Gemini 2.5 Pro

## 🪨 Architecture

### 📄 Agent Workflow
![alt text](<Agent System 2.png>)

### Agents Defined

#### Fetcher

> Uses Gemini to understand the user prompt and fetch a relevant YouTube video via the YouTube Search API

#### Transcriber

> Retrieves the video transcript using youtube-transcript-api

#### Summarizer

> Summarizes transcript into bullet points using Gemini

#### Reviewer

> Polishes summary for clarity, grammar, and flow

#### Formatter

> Outputs the cleaned summary into a formatted PDF using ReportLab

## 📊 Technologies Used

- LangGraph: Workflow orchestration

- Gemini 2.5 Pro: LLM for summarization & review

- YouTube Search & Transcript APIs: Video metadata and subtitles

- ReportLab: PDF generation

- Pydantic: Structured state management

## 📁 Project Structure

youtube-summarizer/
├── agents/
│   ├── fetcher.py
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── reviewer.py
│   └── formatter.py
├── schema.py
├── main.py
├── .env
└── README.md

## 📈 Goal

This project serves as a proof of concept for fast, intelligent, LLM-powered automation.