(function($) {

    $.fn.generateTimetable = function(schedule) {
        var $self = this;

        var init = function() {
            var timetable = new Timetable(),
                startTimeHour = schedule.startTime.split(':')[0],
                endTimeHour = schedule.endTime.split(':')[0];

            timetable.setScope(parseInt(startTimeHour, 10), parseInt(endTimeHour, 10));
            timetable.addDays(schedule.work_days);
            schedule.events.forEach(function(event){
                timetable.addEvent(event.name, event.color, event.day, event.start, event.finish, event.coach, event.info);
            });
            var renderer = new Timetable.Renderer(timetable);
            renderer.draw('#' + $self[0].id);
            return this;
        };
        return init();
    };

}(window.jQuery));
