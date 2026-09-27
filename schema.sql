-- ========================================================
-- CADENCE: PERSONAL FITNESS & DAILY GOAL TRACKING APP
-- Database Schema for Personal Supabase Project: ulpmuwcxcbrcmbkfmrvc
-- ========================================================

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. GOALS DEFINITION TABLE
-- Stores user-configured dynamic daily goals
CREATE TABLE IF NOT EXISTS public.goals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    description TEXT,
    scheduled_time TIME,
    repeat_days TEXT[] DEFAULT ARRAY['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'],
    is_active BOOLEAN NOT NULL DEFAULT true,
    reminders_enabled BOOLEAN NOT NULL DEFAULT true,
    category TEXT DEFAULT 'Routine',
    streak_count INT DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc', now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc', now())
);

-- 2. DAILY GOAL TRACKING TABLE
-- Decoupled execution records preserving historical accuracy
CREATE TABLE IF NOT EXISTS public.daily_goal_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    record_date DATE NOT NULL DEFAULT CURRENT_DATE,
    goal_id UUID REFERENCES public.goals(id) ON DELETE SET NULL,
    goal_title_snapshot TEXT NOT NULL,
    is_completed BOOLEAN NOT NULL DEFAULT false,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc', now()),
    CONSTRAINT unique_daily_goal UNIQUE (record_date, goal_id)
);

-- 3. DAILY NOTES / REASONS TABLE
-- Captures comments, reasons for missed goals, or evening reflections
CREATE TABLE IF NOT EXISTS public.daily_notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    note_date DATE NOT NULL DEFAULT CURRENT_DATE,
    goal_id UUID REFERENCES public.goals(id) ON DELETE SET NULL,
    goal_title TEXT,
    note_text TEXT NOT NULL,
    note_type TEXT DEFAULT 'missed_reason', -- 'missed_reason' or 'evening_reflection'
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc', now())
);

-- 4. DAILY SPARKS / MOTIVATION QUOTES & PHOTOS TABLE
-- Holds 1,000 curated motivational quotes paired with high-resolution scenic photography
CREATE TABLE IF NOT EXISTS public.daily_sparks (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT DEFAULT '#Consistency',
    image_url TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc', now())
);

-- Indexes for high-speed calendar and date-wise queries
CREATE INDEX IF NOT EXISTS idx_daily_records_date ON public.daily_goal_records(record_date);
CREATE INDEX IF NOT EXISTS idx_daily_notes_date ON public.daily_notes(note_date);
CREATE INDEX IF NOT EXISTS idx_goals_active ON public.goals(is_active);
CREATE INDEX IF NOT EXISTS idx_daily_sparks_id ON public.daily_sparks(id);

-- Enable Row Level Security (RLS)
ALTER TABLE public.goals ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.daily_goal_records ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.daily_notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.daily_sparks ENABLE ROW LEVEL SECURITY;

-- Allow full access for personal app (anon / authenticated)
DROP POLICY IF EXISTS "Allow public all access on goals" ON public.goals;
CREATE POLICY "Allow public all access on goals" ON public.goals
    FOR ALL USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Allow public all access on daily_goal_records" ON public.daily_goal_records;
CREATE POLICY "Allow public all access on daily_goal_records" ON public.daily_goal_records
    FOR ALL USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Allow public all access on daily_notes" ON public.daily_notes;
CREATE POLICY "Allow public all access on daily_notes" ON public.daily_notes
    FOR ALL USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Allow public all access on daily_sparks" ON public.daily_sparks;
CREATE POLICY "Allow public all access on daily_sparks" ON public.daily_sparks
    FOR ALL USING (true) WITH CHECK (true);

-- ========================================================
-- INITIAL SEED DATA (Your Cadence Daily Rituals)
-- ========================================================
INSERT INTO public.goals (name, description, scheduled_time, repeat_days, is_active, reminders_enabled, streak_count)
VALUES 
    ('Morning Trail Run', '5.2 km outdoor run', '07:00:00', ARRAY['mon','tue','wed','thu','fri','sat','sun'], true, true, 14),
    ('Hydration Sanctuary', 'Drink at least 2.5L water daily', '08:00:00', ARRAY['mon','tue','wed','thu','fri','sat','sun'], true, true, 28),
    ('Core Mobility & Breathwork', '20 min recovery session', '21:30:00', ARRAY['mon','wed','fri','sun'], true, true, 9),
    ('30 Min Deep Study', 'Architecture and systems focus', '18:00:00', ARRAY['mon','tue','wed','thu','fri','sat','sun'], true, true, 21),
    ('Sleep Before 11:00 PM', 'Screens dimmed at 10:30 PM, sleep by 11 PM', '23:00:00', ARRAY['mon','tue','wed','thu','fri','sat','sun'], true, true, 7)
ON CONFLICT DO NOTHING;
