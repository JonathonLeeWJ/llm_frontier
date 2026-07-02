{
  "name": "support_intent_hard",
  "task_type": "classification",
  "prompt_template": "Classify the support ticket by the customer's TRUE underlying intent, as exactly one of: Billing, Bug, FeatureRequest, HowTo, Cancellation. Judge the real intent, not surface keywords (e.g. a message that mentions cancelling but is really reporting a broken feature is a Bug). Respond with only the label.\nTicket: {input}\nLabel:",
  "subset_match": false,
  "examples": [
    {
      "input": "Your competitor has a calendar view. Any chance of building something similar?",
      "expected": "FeatureRequest"
    },
    {
      "input": "Honestly if you can't fix the sync issue I'm going to cancel \u2014 it's been broken for a week.",
      "expected": "Bug"
    },
    {
      "input": "Can the reports be scheduled to email automatically each Monday? That feature would save hours.",
      "expected": "FeatureRequest"
    },
    {
      "input": "My subscription renewed but I thought I turned off auto-renew. Can I get that reversed?",
      "expected": "Billing"
    },
    {
      "input": "Walk me through setting up a recurring report, please.",
      "expected": "HowTo"
    },
    {
      "input": "Please cancel my subscription, I no longer need the service.",
      "expected": "Cancellation"
    },
    {
      "input": "My annual plan was charged monthly by mistake, I think.",
      "expected": "Billing"
    },
    {
      "input": "Do I get a refund for the unused portion if I cancel mid-cycle?",
      "expected": "Billing"
    },
    {
      "input": "I'm done with this, close my account \u2014 though honestly the crashes are why.",
      "expected": "Cancellation"
    },
    {
      "input": "It would be amazing to have keyboard shortcuts for common actions.",
      "expected": "FeatureRequest"
    },
    {
      "input": "I was charged twice this month and my card shows two identical amounts. Please refund one.",
      "expected": "Billing"
    },
    {
      "input": "Notifications stopped arriving entirely since Tuesday. Nothing changed on my end.",
      "expected": "Bug"
    },
    {
      "input": "Is there a way to merge two projects into one? Not sure if that is possible.",
      "expected": "HowTo"
    },
    {
      "input": "Cancel everything. I found another tool that actually works.",
      "expected": "Cancellation"
    },
    {
      "input": "Can you add Spanish language support? Half my team needs it.",
      "expected": "FeatureRequest"
    },
    {
      "input": "A print-friendly view of reports would be really useful.",
      "expected": "FeatureRequest"
    },
    {
      "input": "I want out \u2014 cancel the account, the missing features make it useless to us.",
      "expected": "Cancellation"
    },
    {
      "input": "I can't figure out how to invite a teammate. Is there a guide?",
      "expected": "HowTo"
    },
    {
      "input": "The invoice says $49 but I was on the $29 plan. Something is wrong with the amount.",
      "expected": "Billing"
    },
    {
      "input": "It would help a lot if we could bulk-upload contacts via CSV.",
      "expected": "FeatureRequest"
    },
    {
      "input": "Every time I click export the app freezes and I lose my work. This has happened five times today.",
      "expected": "Bug"
    },
    {
      "input": "Please add support for two-factor authentication, security matters to us.",
      "expected": "FeatureRequest"
    },
    {
      "input": "I see a charge from you I do not recognise on my statement. What is it for?",
      "expected": "Billing"
    },
    {
      "input": "What's the correct way to archive old records without deleting them?",
      "expected": "HowTo"
    },
    {
      "input": "I'm cancelling because it's too expensive, but I might come back if you had a cheaper tier.",
      "expected": "Cancellation"
    },
    {
      "input": "How do I reset my password? The link in the email does nothing.",
      "expected": "HowTo"
    },
    {
      "input": "I want to close my account and stop all future payments effective immediately.",
      "expected": "Cancellation"
    },
    {
      "input": "The timezone on scheduled posts is wrong, everything publishes an hour late.",
      "expected": "Bug"
    },
    {
      "input": "I keep getting logged out randomly mid-session \u2014 is this a known problem?",
      "expected": "Bug"
    },
    {
      "input": "Any plans to offer an API? We want to integrate with our internal tools.",
      "expected": "FeatureRequest"
    },
    {
      "input": "Please stop billing me, I cancelled last month but was charged again.",
      "expected": "Billing"
    },
    {
      "input": "How can I see who on my team edited a document last?",
      "expected": "HowTo"
    },
    {
      "input": "Uploads over 10MB silently fail with no error message. Please look into it.",
      "expected": "Bug"
    },
    {
      "input": "The mobile app crashes on startup after the latest update. Android 14.",
      "expected": "Bug"
    },
    {
      "input": "I don't understand how to set permissions for a guest user.",
      "expected": "HowTo"
    },
    {
      "input": "The numbers in the dashboard don't match the CSV export \u2014 one of them must be miscalculating.",
      "expected": "Bug"
    },
    {
      "input": "I was promised a discount that never appeared on my invoice.",
      "expected": "Billing"
    },
    {
      "input": "It would be great if you could add a dark mode, my eyes hurt at night.",
      "expected": "FeatureRequest"
    },
    {
      "input": "Where do I find my past invoices to download for accounting?",
      "expected": "HowTo"
    },
    {
      "input": "I need to update the credit card on file before the next billing cycle.",
      "expected": "Billing"
    },
    {
      "input": "How do I connect my Google account? I clicked connect but nothing happens.",
      "expected": "Bug"
    },
    {
      "input": "Where in the settings do I change my notification preferences? I cannot find it.",
      "expected": "HowTo"
    },
    {
      "input": "The search returns no results even for items I know exist. Broken index?",
      "expected": "Bug"
    },
    {
      "input": "Cancel my trial before it converts, I don't want to be charged.",
      "expected": "Cancellation"
    },
    {
      "input": "Why was I billed in USD when my account is set to EUR? The conversion looks off.",
      "expected": "Billing"
    },
    {
      "input": "Could you make the sidebar collapsible? It takes up too much space.",
      "expected": "FeatureRequest"
    },
    {
      "input": "We're switching providers at end of month, please terminate our contract.",
      "expected": "Cancellation"
    },
    {
      "input": "The app shows a white screen after login on Safari specifically.",
      "expected": "Bug"
    },
    {
      "input": "I'd like to downgrade rather than cancel \u2014 is there a smaller plan?",
      "expected": "Billing"
    },
    {
      "input": "How do I export just a date range rather than everything?",
      "expected": "HowTo"
    }
  ]
}