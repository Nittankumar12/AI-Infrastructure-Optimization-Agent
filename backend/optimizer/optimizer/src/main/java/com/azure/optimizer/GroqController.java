package com.azure.optimizer;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:3000") // Allow frontend calls
public class GroqController {

    private final GroqService groqService;

    public GroqController(GroqService groqService) {
        this.groqService = groqService;
    }

    @PostMapping("/analyze")
    public ResponseEntity<Map<String, String>> analyzeInfrastructure(
            @RequestParam("infraFile") MultipartFile infraFile,
            @RequestParam("usageFile") MultipartFile usageFile,
            @RequestParam("prompt") String prompt) {

        String recommendations = groqService.processDataAndGetRecommendations(infraFile, usageFile, prompt);

        Map<String, String> response = new HashMap<>();
        response.put("recommendations", recommendations);

        return ResponseEntity.ok(response);
    }
}