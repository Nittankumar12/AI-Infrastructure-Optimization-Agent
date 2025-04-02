package com.azure.optimizer;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

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
    public ResponseEntity<Map<String, String>> analyzeInfrastructure(@RequestParam("prompt") String prompt) {
        String recommendations = groqService.processDataAndGetRecommendations(prompt);

        Map<String, String> response = new HashMap<>();
        response.put("recommendations", recommendations);

        return ResponseEntity.ok(response);
    }
}
