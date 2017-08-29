"use strict";

var Timetable = function() {
    this.scope = {
        hourStart: 9,
        hourEnd: 17
    };
    this.days = [];
    this.events = [];
};

Timetable.Renderer = function(tt) {
    if (!(tt instanceof Timetable)) {
        throw new Error('Initialize renderer using a Timetable');
    }
    this.timetable = tt;
};


(function() {
    function isValidHourRange(start, end) {
        return isValidHour(start) && isValidHour(end);
    }

    function isValidHour(number) {
        return isInt(number) && isInHourRange(number);
    }

    function isInt(number) {
        return number === parseInt(number, 10);
    }

    function isInHourRange(number) {
        return number >= 0 && number < 24;
    }

    function dayExistsIn(day, days) {
        return days.indexOf(day) !== -1;
    }

    function isValidTimeRange(start, end) {
        var correctTypes = start instanceof Date && end instanceof Date;
        var correctOrder = start < end;
        return correctTypes && correctOrder;
    }

    function getDurationHours(startHour, endHour) {
        return endHour >= startHour ? endHour - startHour : 24 + endHour - startHour;
    }


    Timetable.prototype = {
        setScope: function(start, end) {
            if (isValidHourRange(start, end)) {
                this.scope.hourStart = start;
                this.scope.hourEnd = end;
            } else {
                throw new RangeError('Timetable scope should consist of (start, end) in whole hours from 0 to 23');
            }

            return this;
        },
        addDays: function(newDays) {
            function hasProperFormat() {
                return newDays instanceof Array;
            }

            var existingDays = this.days;
            if (hasProperFormat()) {
                newDays.forEach(function(day) {
                    if (!dayExistsIn(day, existingDays)) {
                        existingDays.push(day);
                    } else {
                        throw new Error('Day already exists');
                    }
                });
            } else {
                throw new Error('Tried to add days in wrong format. Should to be Array');
            }

            return this;
        },
        addEvent: function(name, color, day, start, end, coach, info, options) {
            if (!dayExistsIn(day, this.days)) {
                throw new Error('Unknown day');
            }
            if (!isValidTimeRange(start, end)) {
                throw new Error('Invalid time range: ' + JSON.stringify([start, end]));
            }
            var optionsHasValidType = Object.prototype.toString.call(options) === '[object Object]';
            this.events.push({
                name: name,
                color: color,
                day: day,
                startDate: start,
                endDate: end,
                coach: coach,
                info: info,
                options: optionsHasValidType ? options : undefined
            });

            return this;
        }
    };

    function emptyNode(node) {
        while (node.firstChild) {
            node.removeChild(node.firstChild);
        }
    }

    function prettyFormatHour(hour) {
        var prefix = hour < 10 ? '0' : '';
        return prefix + hour + ':00';
    }


    Timetable.Renderer.prototype = {
        draw: function(selector) {
            function checkContainerPrecondition(container) {
                if (container === null) {
                    throw new Error('Timetable container not found');
                }
            }

            function appendTimetableAside(container) {
                var asideNode = container.appendChild(document.createElement('aside'));
                var timeNode = asideNode.appendChild(document.createElement('time'));
                appendRowHeaders(timeNode);
            }

            function appendRowHeaders(node) {
                var timeULNode = node.appendChild(document.createElement('ul'));
                var completed = false;
                var looped = false;

                for (var hour = timetable.scope.hourStart; !completed;) {

                    if (hour === timetable.scope.hourEnd && (timetable.scope.hourStart !== timetable.scope.hourEnd || looped)) {
                        completed = true;
                        break;
                    }
                    var liNode = timeULNode.appendChild(document.createElement('li'));
                    var spanNode = liNode.appendChild(document.createElement('span'));
                    spanNode.className = 'time-label';
                    spanNode.textContent = prettyFormatHour(hour);
                    if (++hour === 24) {
                        hour = 0;
                        looped = true;
                    }
                }
            }

            function appendTimetableSection(container) {
                var sectionNode = container.appendChild(document.createElement('section'));
                appendColumnHeaders(sectionNode);
                appendDayColumns(sectionNode);
            }

            function appendColumnHeaders(node) {
                var headerNode = node.appendChild(document.createElement('header'));
                var headerULNode = headerNode.appendChild(document.createElement('ul'));

                for (var i = 0; i < timetable.days.length; i++) {
                    var liNode = headerULNode.appendChild(document.createElement('li'));
                    var spanNode = liNode.appendChild(document.createElement('span'));
                    spanNode.className = 'column-heading';
                    spanNode.textContent = timetable.days[i];
                }
            }

            function appendDayColumns(node) {
                var ulNode = node.appendChild(document.createElement('ul'));
                ulNode.className = 'room-timeline';
                for (var i = 0; i < timetable.days.length; i++) {
                    var liNode = ulNode.appendChild(document.createElement('li'));
                    appendDayEvents(timetable.days[i], liNode);
                }
            }

            function appendDayEvents(day, node) {
                for (var i = 0; i < timetable.events.length; i++) {
                    var event = timetable.events[i];
                    if (event.day === day) {
                        appendEvent(event, node);
                    }
                }
            }

            function appendEvent(event, node) {
                var hasOptions = event.options !== undefined;
                var hasURL, hasAdditionalClass, hasDataAttributes = false;
                var hasCoach = event.coach !== undefined;
                var hasAdditionalInfo = event.info !== undefined;

                if (hasOptions) {
                    hasURL = event.options.url !== undefined;
                    hasAdditionalClass = event.options.class !== undefined;
                    hasDataAttributes = event.options.data;
                }

                //var elementType = hasURL ? 'a' : 'span';
                var elementType = 'span';
                var aNode = node.appendChild(document.createElement(elementType));
                var smallNode = aNode.appendChild(document.createElement('small'));
                aNode.title = event.name;
                if (hasCoach) {
                    var smallCoachNode = aNode.appendChild(document.createElement('small'));
                    smallCoachNode.textContent = event.coach;
                    smallCoachNode.className = 'event-coach';
                }
                if (hasAdditionalInfo) {
                    var smallAdditionalNode = aNode.appendChild(document.createElement('small'));
                    smallAdditionalNode.textContent = event.info;
                    smallAdditionalNode.className = 'event-info';
                }
                if (hasURL) {
                    aNode.href = event.options.url;
                }
                if (hasDataAttributes) {
                    for (var key in event.options.data) {
                        aNode.setAttribute('data-' + key, event.options.data[key]);
                    }
                }
                aNode.className = hasAdditionalClass ? 'time-entry ' + event.options.class : 'time-entry';
                aNode.style.height = computeEventBlockHeight(event);
                aNode.style.top = computeEventBlockOffset(event);
                aNode.style.backgroundColor = event.color;
                smallNode.textContent = event.name;
                smallNode.className = 'event-name';
            }

            function computeEventBlockHeight(event) {
                var start = event.startDate;
                var end = event.endDate;
                var durationHours = computeDurationInHours(start, end);
                return durationHours / scopeDurationHours * 100 + '%';
            }

            function computeDurationInHours(start, end) {
                return (end.getTime() - start.getTime()) / 1000 / 60 / 60;
            }

            function computeEventBlockOffset(event) {
                var scopeStartHours = timetable.scope.hourStart;
                var eventStartHours = event.startDate.getHours() + (event.startDate.getMinutes() / 60);
                var hoursBeforeEvent = getDurationHours(scopeStartHours, eventStartHours);
                return hoursBeforeEvent / scopeDurationHours * 100 + '%';
            }

            var timetable = this.timetable;
            var scopeDurationHours = getDurationHours(timetable.scope.hourStart, timetable.scope.hourEnd);
            var container = document.querySelector(selector);
            checkContainerPrecondition(container);
            emptyNode(container);
            appendTimetableAside(container);
            appendTimetableSection(container);
        }
    };

})();
