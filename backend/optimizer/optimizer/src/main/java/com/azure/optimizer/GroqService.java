package com.azure.optimizer;

import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionResult;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.service.OpenAiService;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class GroqService {

    private final OpenAiService openAiService;

    public GroqService() {
        String apiKey = System.getenv("GROQ_API_KEY");
        System.out.println(apiKey);
        this.openAiService = new OpenAiService(apiKey);
    }

    public String processDataAndGetRecommendations(MultipartFile infraFile, MultipartFile usageFile, String prompt) {
        try {
            String infraData = new BufferedReader(new InputStreamReader(infraFile.getInputStream()))
                    .lines().collect(Collectors.joining("\n"));

            String usageData = new BufferedReader(new InputStreamReader(usageFile.getInputStream()))
                    .lines().collect(Collectors.joining("\n"));

            String fullPrompt = "Here is the organization's infrastructure:\n" + infraData +
                                "\n\nHere is its usage data:\n" + usageData +
                                "\n\nUser's optimization request: " + prompt +
                                "\n\nProvide cost and performance improvements.";

            CompletionRequest request = CompletionRequest.builder()
                    .model("llama3-8b-8192")
                    .prompt(fullPrompt)
                    .maxTokens(500)
                    .temperature(0.7)
                    .build();

            return openAiService.createCompletion(request).getChoices().get(0).getText();
        } catch (Exception e) {
            e.printStackTrace();
            return "Error processing data.";
        }
    }
}