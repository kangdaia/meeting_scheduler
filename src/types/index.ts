export interface Todo {
    id: string;
    title: string;
    completed: boolean;
    dueDate?: Date;
    priority: 'high' | 'medium' | 'low';
}

export interface DashboardSummary {
    totalEvents: number;
    upcomingEvents: number;
    completedTodos: number;
    pendingTodos: number;
}

export interface UpcomingEvent {
    id: string;
    title: string;
    start: Date;
    end: Date;
    type: 'event' | 'todo';
    priority?: 'high' | 'medium' | 'low';
}

export interface Event {
    id: string;
    title: string;
    description?: string;
    start: Date;
    end: Date;
    allDay?: boolean;
    color?: string;
}

export interface CalendarViewProps {
    view: 'month' | 'week' | 'day';
    date: Date;
    events: Event[];
}

export interface EventFormData {
    title: string;
    description?: string;
    start: Date;
    end: Date;
    allDay: boolean;
    color?: string;
}